from colorama import Fore

def getG():
    print(Fore.CYAN + "\nTiện ích của tool gathering")
    print(Fore.CYAN + "/help để biết thêm chi tiết\n")
    print(Fore.RED + "Do hiện tại phải tiết kiệm nên các tiện ích có thể sẽ tự động tắt nếu CPU vượt quá 85%\n")

def helpGathering():
    print(Fore.LIGHTYELLOW_EX + "Hướng dẫn sử dụng tiện ích:\n")
    print("/location - Lấy vị trí của IP")  
    print("/header - Lấy Header từ trang Web")
    print("/hostname - Lấy IP từ hostname")
    print(Fore.RED + "/exit - để thoát khỏi tiện ích")