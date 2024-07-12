from menu import menuBase
import os, sys
from colorama import Fore

def main():    
    os.system("cls")
    menuBase.menu()

def stop():
    os.system("cls")
    print(Fore.WHITE)
    sys.exit()

if __name__ == '__main__':    
    main()
    