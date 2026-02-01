import os
import sys
import time
import datetime
import urllib.request

# ================= FILES =================
SECURITY_LOG = "security.log"

# ================= COLORS =================
COLORS = {
    "blue": "\033[94m",
    "green": "\033[92m",
    "purple": "\033[95m",
    "red": "\033[91m"
}
RESET = "\033[0m"

def cprint(text, theme="blue"):
    print(COLORS.get(theme, COLORS["blue"]) + text + RESET)

# ================= UTILS =================
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def get_public_ip():
    try:
        return urllib.request.urlopen("https://api.ipify.org", timeout=3).read().decode()
    except:
        return "UNKNOWN"

def log_session(username):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ip = get_public_ip()
    with open(SECURITY_LOG, "a") as f:
        f.write(f"[{now}] USER: {username} | IP: {ip}\n")

# ================= MALWARE SCANNER =================
SUSPICIOUS_PATTERNS = [
    "eval(", "exec(", "os.system", "subprocess",
    "socket", "base64", "requests",
    "rm -rf", "powershell", "wget", "curl"
]

def scan_for_malware():
    print("\n🛡️ Malware scan started...\n")
    found = False

    for file in os.listdir("."):
        if file.endswith((".py", ".sh", ".bat", ".txt")):
            try:
                with open(file, "r", errors="ignore") as f:
                    content = f.read().lower()
                    for pattern in SUSPICIOUS_PATTERNS:
                        if pattern in content:
                            print(f"⚠️ Suspicious pattern in {file} → {pattern}")
                            found = True
            except:
                pass

    if not found:
        print("✅ No suspicious files found.")
    else:
        print("\n⚠️ Scan finished with warnings.")

# ================= ASCII LOGO =================
LOGO = r"""
                                                    ,----..               
  ,--,                        ,---,       ___      /   /   \   .--.--.    
,--.'|     ,--,             ,--.' |     ,--.'|_   /   .     : /  /    '.  
|  | :   ,--.'|             |  |  :     |  | :,' .   /   ;.  \  :  /`. /  
:  : '   |  |,     ,----._,.:  :  :     :  : ' :.   ;   /  ` ;  |  |--`   
|  ' |   `--'_    /   /  ' /:  |  |,--.;__,'  / ;   |  ; \ ; |  :  ;_     
'  | |   ,' ,'|  |   :     ||  :  '   |  |   |  |   :  | ; | '\  \    `.  
|  | :   '  | |  |   | .\  .|  |   /' :__,'| :  .   |  ' ' ' : `----.   \ 
'  : |__ |  | :  .   ; ';  |'  :  | | | '  : |__'   ;  \; /  | __ \  \  | 
|  | '.'|'  : |__'   .   . ||  |  ' | : |  | '.'|\   \  ',  / /  /`--'  / 
;  :    ;|  | '.'|`---`-'| ||  :  :_:,' ;  :    ; ;   :    / '--'.     /  
|  ,   / ;  :    ;.'__/\_: ||  | ,'     |  ,   /   \   \ .'    `--'---'   
 ---`-'  |  ,   / |   :    :`--''        ---`-'     `---`                 
          ---`-'   \   \  /                                               
                    `--`-'                                                
"""

# ================= LOGIN =================
def login():
    clear()
    print("=== lightOS LOGIN ===\n")

    users = {
        "admin": "admin2013",
        "user": "user123"
    }

    for _ in range(3):
        username = input("Username: ")
        password = input("Password: ")

        if username in users and users[username] == password:
            log_session(username)
            return username

        print("❌ Invalid credentials.\n")

    sys.exit("Too many failed attempts.")

# ================= HELP =================
def show_help():
    print("""
help   - Show commands
list   - List files
open   - Open text file
calc   - Calculator
google - Google search
myip   - Show your public IP
scan   - Scan files for malware
update - Update lightOS
color  - Change color theme
clear  - Clear screen
exit   - Exit lightOS
""")

# ================= MAIN OS =================
def lightos(username):
    theme = "blue"
    clear()

    # Top-right credit
    cols = os.get_terminal_size().columns
    print("Made by Matej Toseski".rjust(cols))
    print()

    cprint(LOGO, theme)

    if username == "admin":
        cprint("Welcome back admin 🚀", theme)
    else:
        cprint("Welcome to lightOS 🚀", theme)

    show_help()

    while True:
        cmd = input("\nlightOS> ").strip().lower()

        if cmd == "help":
            show_help()

        elif cmd == "clear":
            clear()
            print("Made by Matej Toseski".rjust(cols))
            print()
            cprint(LOGO, theme)
            show_help()

        elif cmd == "list":
            for f in os.listdir("."):
                print(f)

        elif cmd == "open":
            name = input("File name: ")
            if os.path.exists(name):
                with open(name, "r", errors="ignore") as f:
                    print(f.read())
            else:
                print("File not found.")

        elif cmd == "calc":
            expr = input("Enter calculation: ")
            try:
                print(eval(expr))
            except:
                print("Invalid expression.")

        elif cmd == "google":
            q = input("Search: ")
            print(f"Google search (simulated): {q}")

        elif cmd == "myip":
            print("Your IP:", get_public_ip())

        elif cmd == "scan":
            scan_for_malware()

        elif cmd == "update":
            print("Checking for updates...")
            time.sleep(1)
            print("lightOS is up to date!")

        elif cmd == "color":
            new = input("Choose theme (blue/green/purple/red): ").lower()
            if new in COLORS:
                theme = new
                print("Theme changed.")
            else:
                print("Invalid theme.")

        elif cmd == "exit":
            print("\nGood bye, see you soon! 👋")
            time.sleep(1)
            break

        else:
            print("Unknown command. Type 'help'.")

# ================= BOOT =================
if __name__ == "__main__":
    user = login()
    lightos(user)
