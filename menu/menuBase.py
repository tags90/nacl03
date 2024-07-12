from tools import gathering
from info import help, aboutme


def menu():
    
    option = input("Hay nhap lenh >>> ")

    while option != "/exit":
        print("\n===================================================\n")
        if option == "/help":
            help.show_help()

        elif option == "/about":
            aboutme.about()

        elif option == "/thuthapthongtinweb":
            # In ra chức năng thứ 1
            print('Đang chạy chức năng thu thập')
            # Nhập các chức năng 
            g = gathering.Gathering()
            g.getHeader()

        else:
            print("\n\n\nNhập ngu. Vui lòng nhập lại")
        
        # Ngắt phần chạy menu        
        menu()
        
    
    # In ra thông báo đã sử dụng tool
    print("\n\n\nBye bye. Cám ơn vì đã dùng tới tao\n\n\n")
