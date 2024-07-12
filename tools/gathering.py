import requests

class Gathering:

    def __init__(self, url=None):
        self.url = url
    
    def getURL(self):
        return self.url
    
    def setURL(self, value):
        self.url = input("Nhập URL " + value + ": ")
        return self.getURL()
    
    def getHeader(self):
        if self.url is None:
            self.setURL("mới")  # Hoặc bất kỳ chuỗi nào bạn muốn nhắc người dùng
        r = requests.get(self.getURL())
        print(r.headers)

# Ví dụ sử dụng:
# gathering = Gathering()
# gathering.getHeader()
