from utils.Constants import CMD_COLOR_RED, CMD_COLOR_DEFAULT, CMD_COLOR_BLUE, CMD_COLOR_YELLOW, CMD_COLOR_CYAN


def input_menu_choice(message="Enter your choice: "):
    try:
        choice = int(input(message))
        return choice
    except ValueError:
        return None


def print_title(message="Menu"):
    print(f"{CMD_COLOR_YELLOW}{message}{CMD_COLOR_DEFAULT}")


def print_error(message="Error occurred"):
    print(f"{CMD_COLOR_RED}{message}{CMD_COLOR_DEFAULT}")


def print_info(message="Info Message"):
    print(f"{CMD_COLOR_BLUE}{message}{CMD_COLOR_DEFAULT}")


def print_welcome():
    print(f'''{CMD_COLOR_CYAN}\n                                                                                                                                                                                                                                                             
                        ...                                            ...                                                                            s    
                     xH88"`~ .x8X                                   xH88"`~ .x8X                                                                     :8    
                   :8888   .f"8888Hf                .u    .       :8888   .f"8888Hf        u.      u.    u.      u.    u.                           .88    
                  :8888>  X8L  ^""`        u      .d88B :@8c     :8888>  X8L  ^""`   ...ue888b   x@88k u@88c.  x@88k u@88c.      .u          .     :888ooo 
                  X8888  X888h          us888u.  ="8888f8888r    X8888  X888h        888R Y888r ^"8888""8888" ^"8888""8888"   ud8888.   .udR88N  -*8888888 
                  88888  !88888.     .@88 "8888"   4888>'88"     88888  !88888.      888R I888>   8888  888R    8888  888R  :888'8888. <888'888k   8888    
                  88888   %88888     9888  9888    4888> '       88888   %88888      888R I888>   8888  888R    8888  888R  d888 '88%" 9888 'Y"    8888    
                  88888 '> `8888>    9888  9888    4888>         88888 '> `8888>     888R I888>   8888  888R    8888  888R  8888.+"    9888        8888    
                  `8888L %  ?888   ! 9888  9888   .d888L .+      `8888L %  ?888   ! u8888cJ888    8888  888R    8888  888R  8888L      9888       .8888Lu= 
                   `8888  `-*""   /  9888  9888   ^"8888*"        `8888  `-*""   /   "*888*P"    "*88*" 8888"  "*88*" 8888" '8888c. .+ ?8888u../  ^%888*   
                     "888.      :"   "888*""888"     "Y"            "888.      :"      'Y"         ""   'Y"      ""   'Y"    "88888%    "8888P'     'Y"    
                       `""***~"`      ^Y"   ^Y'                       `""***~"`                                                "YP'       "P'              
    ''')
    print(f"                                                           Welcome to CarConnect - A place to rent and manage cars\n{CMD_COLOR_DEFAULT}")
