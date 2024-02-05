
class color:
    DEFINED_COLORS = [ 
                        "red", "orange", "green", "lime", 
                        "yellow", "blue", "dark_blue", "pink", 
                        "purple", "gray", "cyan", "lavendar",
                        "black"
                     ]
    RED = '\033[91m'
    ORANGE = '\033[38;5;214m'
    GREEN = '\033[92m'
    LIME = '\033[38;5;120m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    DARK_BLUE = '\033[38;5;18m'
    PINK = '\033[38;5;207m'
    PURPLE = '\033[38;5;171m'
    GRAY = '\033[38;5;245m'
    CYAN = '\033[38;5;51m'
    BLACK = '\033[30m'



    DEFINED_BACKGROUNDS = [ 
                        "blue", "pink"
                     ]
    BLUE_BG = '\033[48;5;4m'
    PINK_BG = '\033[48;5;206m'


    END = '\033[0m'




def red_text(var=""):
    if not isinstance(var, (int,float,str)):
        return var
    var = str(var)
    if len(var)==0:
        return ""
    return f'{color.RED}{var}{color.END}'

def orange_text(var=""):
    if not isinstance(var, (int,float,str)):
        return var
    var = str(var)
    if len(var)==0:
        return ""
    return f'{color.ORANGE}{var}{color.END}'
    
def green_text(var=""):
    if not isinstance(var, (int,float,str)):
        return var
    var = str(var)
    if len(var)==0:
        return ""
    return f'{color.GREEN}{var}{color.END}'
 
def lime_text(var=""):
    if not isinstance(var, (int,float,str)):
        return var
    var = str(var)
    if len(var)==0:
        return ""
    return f'{color.LIME}{var}{color.END}'

def yellow_text(var=""):
    if not isinstance(var, (int,float,str)):
        return var
    var = str(var)
    if len(var)==0:
        return ""
    return f'{color.YELLOW}{var}{color.END}'

def blue_text(var=""):
    if not isinstance(var, (int,float,str)):
        return var
    var = str(var)
    if len(var)==0:
        return ""
    return f'{color.BLUE}{var}{color.END}'
    
def dark_blue_text(var=""):
    if not isinstance(var, (int,float,str)):
        return var
    var = str(var)
    if len(var)==0:
        return ""
    return f'{color.DARK_BLUE}{var}{color.END}'
    
def pink_text(var=""):
    if not isinstance(var, (int,float,str)):
        return var
    var = str(var)
    if len(var)==0:
        return ""
    return f'{color.PINK}{var}{color.END}'
    
def purple_text(var=""):
    if not isinstance(var, (int,float,str)):
        return var
    var = str(var)
    if len(var)==0:
        return ""
    return f'{color.PURPLE}{var}{color.END}'
    
def gray_text(var=""):
    if not isinstance(var, (int,float,str)):
        return var
    var = str(var)
    if len(var)==0:
        return ""
    return f'{color.GRAY}{var}{color.END}'
    
def cyan_text(var=""):
    if not isinstance(var, (int,float,str)):
        return var
    var = str(var)
    if len(var)==0:
        return ""
    return f'{color.CYAN}{var}{color.END}'




# BACKGROUND COLORS =========================================

def blue_bg(var=""):
    if not isinstance(var, (int,float,str)):
        return var
    var = str(var)
    if len(var)==0:
        return ""
    return f'{color.BLUE_BG}{var}{color.END}'

def pink_bg(var=""):
    if not isinstance(var, (int,float,str)):
        return var
    var = str(var)
    if len(var)==0:
        return ""
    return f'{color.PINK_BG}{color.BLACK}{var}{color.END}'