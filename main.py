from menu import menuBase
import os, sys

def main():
    print("\n===================================================")
    print("Chào mừng bạn đã đến với TOOLS :3")
    print("/help để biết thêm chi tiết")
    print("===================================================\n")
    os.system("cls")
    menuBase.menu()

def stop():
    os.system("cls")   
    sys.exit()

if __name__ == '__main__':    
    main()
    