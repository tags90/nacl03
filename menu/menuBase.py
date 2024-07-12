import main, os
from colorama import Fore, Style
from info import help, aboutme
from menu import menuGathering



def menu():    
    option = input(Fore.GREEN + "Hay nhap lenh >>> ")
    os.system("cls")

    if option != None:
        while option != "/exit":

            if option == "/help":
                help.show_help()

            elif option == "/about":
                aboutme.about()

            elif option == "/gathering":
                print('Đang chạy chức năng thu thập')
                # Nhập các chức năng            
                menuGathering.menu()

            else:
                print(Fore.RED +"Nhập ngu. Vui lòng nhập lại")
        
            # Ngắt phần chạy menu        
            menu()
        main.stop()
    
        # In ra thông báo đã sử dụng tool
    
    
