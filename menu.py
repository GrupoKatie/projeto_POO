from UI import *
from inventory import Inventory

def start():    
    inv = Inventory()

    
    while(True):
        print(WELCOME_MESSAGE, OPTIONS_MESSAGE)
        
        option = int(input("Opção: "))
    
        options_dict = {
            1: inv.addProduct, 
            2: inv.removeProduct, 
            3: inv.changeProduct, 
            4: inv.reportCategory, 
            5: inv.reportExpiration}
            
        if option in options_dict.keys():
            options_dict[option]()
        else: print(ERROR_MESSAGE)