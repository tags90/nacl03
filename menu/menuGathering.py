from tools import gathering
from info import aboutGathering
from menu import menuBase

g = gathering.Gathering()

def menu():
    print("\nHãy nhập tiện ích\n/getHeader\n/.....")
    ext_option = input("Hãy nhập tiện ích >>>")

    while ext_option != "/exit":
        
        # Điều kiện chọn tiện ích
        if ext_option == "/about":
            aboutGathering.helpGathering()
        
        elif ext_option == "/getHeader":
            g.getHeader()

        menu()
    print ("Quay trở lại")           
    menuBase.menu()        
