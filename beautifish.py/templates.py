import sys
import time
import os
import threading
import pyfiglet

import beautifish.colors as cl 
import beautifish.icons as ic
import beautifish.decorators as dc 

from beautifish.__beautifish_utils__.give_color import __give_color
from beautifish.__beautifish_utils__.recursive_dict_print import __print_tree, __print_list
from beautifish.__beautifish_utils__.user_input import __get_input

DENSITY_MODES = [ "compact", "spaced" ]
DEFINED_COLORS = cl.color.DEFINED_COLORS



# =================================================================
# ===== WARNING ===================================================

def warning(msg:str,title:str="",mode:str="compact"):

    title   = title if title!="" else "Warning"
    msg     = msg   if   msg!="" else "Check the code for faulty behaviors"
    mode    = mode.lower()
    
    if mode.lower() not in DENSITY_MODES:
        print(msg if msg!="" else None)
    
    
    if mode=="compact":
        decorator = f"{ic.WARNING} {title}:"
        decorator = cl.yellow_text(decorator)
        
        msg = cl.gray_text(msg)

        print(f"{decorator} {msg}")

    
    elif mode=="spaced":
        decorator = f"{ic.WARNING}  {title}:"
        decorator = cl.yellow_text(decorator)

        msg = cl.gray_text(msg)
    
        print(f"\n{decorator}\n   {msg}\n")
    


# =================================================================
# ===== DANGER ====================================================

def danger(msg:str,title:str="",mode:str="compact"):
    
    title   = title if title!="" else "DANGER"
    msg     = msg   if   msg!="" else "Proceed with caution"
    mode    = mode.lower()
    
    if mode.lower() not in DENSITY_MODES:
        print(msg if msg!="" else None)
    
    
    if mode=="compact":
        decorator = f"{ic.DANGER} {title}:"
        decorator = cl.orange_text(decorator)
        
        msg = cl.orange_text(msg)

        print(f"{decorator} {msg}")

    
    elif mode=="spaced":
        decorator = f"{ic.DANGER}  {title}:"
        decorator = cl.orange_text(decorator)

        msg = cl.orange_text(msg)
    
        print(f"\n{decorator}\n  {msg}\n")
    


# =================================================================
# ===== SUCCESS ===================================================

def success(msg:str="",title:str="",mode:str="compact"):
    
    title   = title if title!="" else "Success"
    msg     = msg   if   msg!="" else "Successfully executed!!"
    mode    = mode.lower()
    
    if mode.lower() not in DENSITY_MODES:
        print(msg if msg!="" else None)
    
    
    if mode=="compact":
        decorator = f"{ic.TICK} {title}:"
        decorator = cl.green_text(decorator)
        
        msg = cl.lime_text(msg)

        print(f"{decorator} {msg}")

    
    elif mode=="spaced":
        decorator = f"{ic.TICK}  {title}:"
        decorator = cl.green_text(decorator)
    
        print(f"\n{decorator}\n   {msg}\n")



# =================================================================
# ===== ERROR =====================================================
    
def error(msg:str,title:str="",mode:str="compact"):
    
    title   = title if title!="" else "ERROR"
    msg     = msg   if   msg!="" else "There's an error in this code"
    mode    = mode.lower()
    
    if mode.lower() not in DENSITY_MODES:
        print(msg if msg!="" else None)
    
    
    if mode=="compact":
        decorator = f"{ic.CROSS} {title}:"
        decorator = cl.red_text(decorator)
        
        msg = cl.red_text(msg)

        print(f"{decorator} {msg}")

    
    elif mode=="spaced":
        decorator = f"{ic.CROSS}  {title}:"
        decorator = cl.red_text(decorator)

        msg = cl.red_text(msg)
    
        print(f"\n{decorator}\n   {msg}\n")
    


# =================================================================
# ===== NOT FOUND =================================================

def not_found(msg:str="",title:str="",mode:str="compact"):

    title   = title if title!="" else "Not Found"
    msg     = msg   if   msg!="" else "The data was not found..."
    mode    = mode.lower()
    
    if mode.lower() not in DENSITY_MODES:
        print(msg if msg!="" else None)
    
    
    if mode=="compact":
        decorator = f"{ic.CROSS} {title}:"
        decorator = dc.bold(dc.dim(cl.gray_text(decorator)))
        
        msg = dc.dim(cl.gray_text(msg))

        print(f"{decorator} {msg}")

    
    elif mode=="spaced":
        decorator = f"{ic.CROSS}  {title}:"
        decorator = dc.bold(dc.dim(cl.gray_text(decorator)))

        msg = dc.dim(cl.gray_text(msg))
    
        print(f"\n{decorator}\n   {msg}\n")

""" 
# =================================================================
# ===== HEADERS ===================================================

def header1():
    pass

def header2():
    pass

def header3():
    pass
 


# =================================================================
# ===== PROMPT ====================================================

def prompt():
    pass
"""


# =================================================================
# ===== INPUT =====================================================

def input(msg:str="",color:str="pink"):
    if color not in DEFINED_COLORS:
        color = "pink"
        
    response = __get_input(f"{ic.ARROW_RIGHT2} {msg}",color)
    return response


# =================================================================
# ===== SEPERATOR =================================================

def seperator1(header="",color:str="blue"):
    if color not in DEFINED_COLORS:
        color = "blue"

    bash_width = 70
    seperating_line = ("=" * bash_width) if bash_width!=None else ""
    seperating_line = __give_color(seperating_line,color)
    

    if isinstance(header, (int,float,str)) and header!="":
        header = header.upper()
        print(f"\n\n{seperating_line}")
        print(f"{seperating_line[:10]} {header} {seperating_line[ : bash_width - ( len(str(header)) + 2 ) ]}")
        print(f"{seperating_line}\n")

    else:
        print(f"\n\n{seperating_line}")
        print(f"{seperating_line}\n")




def seperator2(header="",color:str="green"):
    if color not in DEFINED_COLORS:
        color = "green"

    bash_width = 40
    seperating_line = (ic.DASH * bash_width) if bash_width!=None else ""
    seperating_line = __give_color(seperating_line,color)
    
    if isinstance(header, (int,float,str)) and header!="":
        header = header.capitalize()
        print(f"\n{seperating_line[:7]} {header} {seperating_line[10:]}\n")
    else:
        print(f"\n{seperating_line}\n")




def seperator3(header="",color:str="gray"):
    if color not in DEFINED_COLORS:
        color = "gray"

    bash_width = 20
    seperating_line = (ic.DOT * bash_width) if bash_width!=None else ""
    seperating_line = __give_color(seperating_line,color)

    if isinstance(header, (int,float,str)) and header!="":
        header = header.lower()
        x = f"\n{seperating_line[:13]} {header} {seperating_line[12:]}\n"
        print(dc.dim(x))
    else:
        print(f"\n{dc.dim(seperating_line)}\n")


# =================================================================
# ===== LSITING =================================================

def tree(data:dict,title:str="",offset:int=0):

    base_offset = 1 + offset
    step = 4

    icons = [ ic.ARROW_RIGHT2, ic.ARROW_RIGHT, ic.DOT, ic.DASH ]
    icon_index = 0

    __print_tree(data,base_offset,step,icons,icon_index)

    

def list(arr:list,title:str="",offset:int=0):

    base_offset = 1 + offset
    step = 1

    __print_list(arr,base_offset,step)

""" 
# =================================================================
# ===== TABLE =====================================================

def table():
    pass
 """

# =================================================================
# ===== SUBTITLE ==================================================

def subtitle():
    pass


# =================================================================
# ===== LOADING BAR ===============================================

def loading_bar(iterations:int,msg:str="",type:str="modern",length:int=50):
    LOADING_BAR_TYPES = [ "modern", "retro" ]

    def loading_action(type:str,iterations:int,length:int=50):
        
        icon = "#"
        if type=="modern":
            icon = ic.DASH

        empty_space = " "
        if type=="modern":
            empty_space = dc.dim(cl.gray_text(ic.DASH))

        print()

        for i in range(iterations+1):
            progress = i/iterations
            
            bar = icon * int(length*progress)
            spaces = empty_space * (length-len(bar))

            percentage = f"{int(progress*100)}%"
            
            if type=="modern":
                bar = cl.purple_text(bar)
                percentage = cl.purple_text(percentage)
                sys.stdout.write(f"\r{msg} {bar}{spaces} {percentage}")
            elif type=="retro":
                sys.stdout.write(f"\r{msg} [{bar}{spaces}] {percentage}")
            
            sys.stdout.flush()
            time.sleep(0.1)

        print("\n")


    msg         = msg   if   msg!="" else "Loading"
    type        = type.lower()


    
    if (type.lower() not in LOADING_BAR_TYPES) or (iterations<=0):
        return msg if msg!="" else "Loading..."
    

    if type=="modern":
        loading_action(iterations=iterations,length=length,type=type)
        return
    
    if type=="retro":
        loading_action(iterations=iterations,length=length,type=type)
        return
    

""" 
# =================================================================
# ===== SPINNER ===================================================

def spinner(msg:str="",type:str="snake"):
    SPINNER_TYPES = [ "snake", "wheel", "slash" ]

    msg     = msg   if   msg!="" else "Loading"
    type    = type.lower()
    
    if type.lower() not in SPINNER_TYPES:
        type="snake"



    def spinning_action(msg:str):
        
        spinner_states = [ "⠴", "⠤", "⠦", "⠇", "⠋", "⠉", "⠙", "⠸"]
        spinner_states = [ cl.cyan_text(state) for state in spinner_states ]
        i = 0
        msg = cl.cyan_text(msg)

        while True:
            print(f"\r{spinner_states[i]} {msg}\n", end="", flush=True)
            time.sleep(0.3)
            i = (i + 1) % len(spinner_states)


    spinning_action(msg) 
    
    
    stop_spinner = threading.Event()

    spinner_thread = threading.Thread(target=spinning_action)
    active_acount = threading.active_count()
    spinner_thread.start()

    time.sleep(6)
    spinner_thread.join() 
    """


# =================================================================
# ===== BANNER ====================================================

def banner(msg:str,color:str="red",offset:int=0):
    if color not in DEFINED_COLORS:
        color = "red"

    if msg=="":
        return ""
    
    spaces = " " * offset
    msg = spaces + msg

    ascii_banner = pyfiglet.figlet_format(msg)
    ascii_banner = __give_color(ascii_banner,color)


    print(f"\n{ascii_banner}\n")
