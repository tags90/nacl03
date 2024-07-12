from tools import gathering
from info import aboutGathering
from menu import menuBase
from colorama import Fore
import os

g = gathering.Gathering()

def menu():
    aboutGathering.getG()
    ext_option = input(Fore.GREEN + "Hãy nhập tiện ích >>>")
    os.system("cls")
    while ext_option != "/exit":
        
        # Điều kiện chọn tiện ích
        if ext_option == "/help":
            aboutGathering.helpGathering()
        
        elif ext_option == "/getHeader":
            g.getHeader()

        menu()
    print ("Quay trở lại")           
    menuBase.menu()        
