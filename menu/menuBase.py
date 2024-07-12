import main, os
from colorama import Fore, Style
from info import help, aboutme, gettingStarted
from menu import menuGathering

def menu():    
    gettingStarted.getStart()

    option = input(Fore.GREEN + "Hay nhap lenh >>> ")
    os.system("cls")

    if option != None:
        while option != "/exit": 

            if option == "/help":
                help.show_help()

            elif option == "/about":
                aboutme.about()

            elif option == "/gathering":
                print(Fore.YELLOW + 'Đang chạy chức năng thu thập')            
                menuGathering.menu()

            else:
                print(Fore.RED +"Nhập ngu quá :))). Vui lòng nhập lại\n")        
            # Ngắt phần chạy menu        
            menu()
        main.stop()
    
    
