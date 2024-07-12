from tools import gathering
from info import aboutGathering
from menu import menuBase
from colorama import Fore
import os

def menu():
    aboutGathering.getG()
    ext_option = input(Fore.GREEN + "Hãy nhập tiện ích >>>")
    os.system("cls")
    while ext_option != "/exit":
        
        # Điều kiện chọn tiện ích
        if ext_option == "/help":
            aboutGathering.helpGathering()
        
        elif ext_option == "/location":
            gathering.Gathering.getLocation()
        
        elif ext_option == "/header":
            gathering.Gathering.getHeader()

        elif ext_option == "/hostname":
            gathering.Gathering.getInternetProtocolFromHostName()

        menu()
    print (Fore.RED+ "Quay trở lại\n")           
    menuBase.menu()        
