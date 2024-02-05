import msvcrt

import beautifish.colors as cl 
from beautifish.__beautifish_utils__.give_color import __give_color, __give_bg
from beautifish.__beautifish_utils__.check_os import __check_os_type

def __get_input(msg:str="",color:str="pink"):
    print(__give_bg(msg,color) + " ",end='',flush=True)

    user_input = ""

    os_type = __check_os_type()

    if os_type.lower()=="windows":
        while True:
            key = msvcrt.getch().decode('utf-8')
            if key == '\r':  # Enter key pressed
                break
            user_input += key
            print(__give_color(key,color), end='', flush=True)

    elif os_type.lower() in [ "linux", "macos" ]:
        import termios
        import tty
        import sys

        original_settings = termios.tcgetattr(sys.stdin)

        try:
            tty.setraw(sys.stdin.fileno())
            user_input = ''
            while True:
                key = sys.stdin.read(1)
                if key == '\r':  # Enter key pressed
                    break
                user_input += key
                print(__give_color(key,color), end='', flush=True)
        finally:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, original_settings)
            

    print()
    return user_input
