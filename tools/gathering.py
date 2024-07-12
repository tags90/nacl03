import requests, socket, json

class Gathering:
    def getHeader():
        url = input("Nhập hostname: ")
        r = requests.get("https://"+ url)
        print(r.headers)

    def getInternetProtocolFromHostName():
        url = input("Nhập hostname: ")
        ip = socket.gethostbyname(url)
        print(f"IP của {url} là {ip}")
    
    def getLocation():
        ip = input("Nhập IP: ")
        r = requests.get("https://ipinfo.io/"+ ip +"/json")
        data = json.loads(r.text)
        print("Vị trí hiện tại của " + ip + " is " + data["loc"])
        

        
