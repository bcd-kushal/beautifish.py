import beautifish.colors as cl

def __give_color(str:str,col:str):
    if str=="" or str==None:
        return 
    
    if col.lower()=="red":
        return cl.red_text(str)
        
    elif col.lower()=="blue":
        return cl.blue_text(str)
        
    elif col.lower()=="red":
        return cl.red_text(str)
        
    elif col.lower()=="pink":
        return cl.pink_text(str)
        
    elif col.lower()=="purple":
        return cl.purple_text(str)
        
    elif col.lower()=="orange":
        return cl.orange_text(str)
        
    elif col.lower()=="lime":
        return cl.lime_text(str)
        
    elif col.lower()=="green":
        return cl.green_text(str)
        
    elif col.lower()=="gray":
        return cl.gray_text(str)
        
    elif col.lower()=="yellow":
        return cl.yellow_text(str)
        
    elif col.lower()=="cyan":
        return cl.cyan_text(str)
    
    else:
        return str
        



def __give_bg(str:str,col:str):
    if str=="" or str==None:
        return 
    
    if col.lower()=="blue":
        return cl.blue_bg(str)
        
    elif col.lower()=="pink":
        return cl.pink_bg(str)
        
    else:
        return str
        