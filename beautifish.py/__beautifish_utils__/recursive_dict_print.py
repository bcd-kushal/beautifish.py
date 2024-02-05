import beautifish.colors as cl
import beautifish.decorators as dc

def __print_tree(data:dict,offset:int,step:int,icons:list,icon_index:int):

    for [ key, val ] in data.items():

        spaces = ""
        for i in range(1,offset+1):
            if (i-2)%step==0:
                spaces += dc.dim(cl.gray_text("│"))
            else:
                spaces += " "

        if not type(val)==dict:
            shell_line = f"{spaces}{icons[icon_index]} {cl.cyan_text(f'{key}:')} {val}"
            print(shell_line)

        else: 
            shell_line = f"{spaces}{icons[icon_index]} {cl.cyan_text(f'{key}: ')}"
            print(shell_line)

            __print_tree(val,offset+step,step,icons,(icon_index+1)%len(icons))

    x = spaces[:len(spaces)-step-1] + f"{dc.dim(cl.gray_text("─"))}"
    last_d = x.rfind("│")
    if last_d > -1:
        x = x[:last_d] + "└" + x[last_d+1:]
    print(x)





def __print_list(arr:list,offset:int,step:int):

    c = 1

    for item in arr:

        spaces = " " * offset

        if not type(item)==list:
            shell_line = f"{spaces}{dc.dim(cl.gray_text(str(c)+'.'))} {item}"
            print(shell_line)
            c += 1

        else: 
            __print_list(item,offset+step,step)
    
    print()
