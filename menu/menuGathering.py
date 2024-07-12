from tools import gathering

g = gathering.Gathering()

ext_option = input()

if ext_option != None:
    while ext_option == "/exit":

        # Bảng thông của tool phải được hiển thị liên tục
        print("/.....\n/.....")
        
        # Điều kiện chọn tiện ích
        if ext_option =="/about":
            print("n")

else: 
    print("lỗi")