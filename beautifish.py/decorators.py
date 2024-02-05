class decorators:

    BOLD            = '\033[1m'
    DIM             = '\033[2m'
    ITALIC          = '\033[3m'
    UNDERLINE       = '\033[4m'
    STRIKETHROUGH   = '\033[9m'
    END             = '\033[0m'


def bold(str:str):
    if str=="":
        return ""
    return f"{decorators.BOLD}{str}{decorators.END}"

def dim(str:str):
    if str=="":
        return ""
    return f"{decorators.DIM}{str}{decorators.END}"

def italic(str:str):
    if str=="":
        return ""
    return f"{decorators.ITALIC}{str}{decorators.END}"

def underline(str:str):
    if str=="":
        return ""
    return f"{decorators.UNDERLINE}{str}{decorators.END}"

def strikethrough(str:str):
    if str=="":
        return ""
    return f"{decorators.STRIKETHROUGH}{str}{decorators.END}"