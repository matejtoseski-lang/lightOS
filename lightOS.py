import os
import webbrowser
import subprocess
import shutil
import urllib.request

# ================= COLORS =================
COLORS = {
    "default": "\033[0m",
    "green": "\033[92m",
    "blue": "\033[94m",
    "red": "\033[91m",
    "purple": "\033[95m",
    "cyan": "\033[96m"
}

CURRENT_COLOR = COLORS["cyan"]

def color(text):
    return CURRENT_COLOR + text + COLORS["default"]

# ================= HEADER =================
def print_header():
    width = shutil.get_terminal_size((80, 20)).columns
    text = "Made by Matej Toseski"
    print(color(text.rjust(width)))

# ================= LOGO =================
def lightos_logo():
    print(color(r"""
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
"""))

# ================= MENU =================
def show_options():
    print(color("""
Commands:
 help            - Show commands
 list            - List files
 open <file>     - Open text file
 calc            - Calculator
 google          - Google search
 myip            - Show your public IP
 update          - Update lightOS
 color           - Change color theme
 clear           - Clear screen
 exit            - Exit lightOS
"""))

# ================= FUNCTIONS =================
def list_files():
    for f in os.listdir():
        print(color(" - " + f))

def open_file(name):
    if not os.path.exists(name):
        print(color("File not found."))
        return
    try:
        with open(name, "r", encoding="utf-8") as f:
            print(color("\n" + f.read()))
    except:
        print(color("Cannot open file."))

def calculator():
    print(color("Calculator (type 'exit' to quit)"))
    while True:
        exp = input("calc> ")
        if exp.lower() == "exit":
            break
        try:
            print(color(str(eval(exp))))
        except:
            print(color("Invalid expression"))

def google():
    q = input("Search Google: ").strip()
    if q:
        webbrowser.open(
            "https://www.google.com/search?q=" + q.replace(" ", "+")
        )

def my_ip():
    try:
        ip = urllib.request.urlopen("https://api.ipify.org").read().decode()
        print(color("Your public IP: " + ip))
    except:
        print(color("Unable to fetch IP."))

def update_lightos():
    if not os.path.exists(".git"):
        print(color("Not a git repository."))
        return
    result = subprocess.run(["git", "pull"], capture_output=True, text=True)
    print(color(result.stdout or result.stderr))

def change_color():
    global CURRENT_COLOR
    print(color("Available colors: green, blue, red, purple, cyan"))
    c = input("Choose color: ").lower()
    if c in COLORS:
        CURRENT_COLOR = COLORS[c]
        print(color("Color changed!"))
    else:
        print(color("Invalid color."))

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# ================= MAIN =================
def main():
    clear()
    print_header()
    lightos_logo()
    print(color("Welcome to lightOS 🚀"))
    show_options()

    while True:
        cmd = input(color("lightOS> ")).strip().split()
        if not cmd:
            continue

        c = cmd[0].lower()

        if c == "help":
            show_options()
        elif c == "list":
            list_files()
        elif c == "open" and len(cmd) > 1:
            open_file(cmd[1])
        elif c == "calc":
            calculator()
        elif c == "google":
            google()
        elif c == "myip":
            my_ip()
        elif c == "update":
            update_lightos()
        elif c == "color":
            change_color()
        elif c == "clear":
            clear()
        elif c == "exit":
            print(color("\nGood bye, see you soon! 👋\n"))
            break
        else:
            print(color("Unknown command. Type 'help'."))

if __name__ == "__main__":
    main()
