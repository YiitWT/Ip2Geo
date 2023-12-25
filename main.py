import requests
from termcolor import colored

print(colored("IP Adress Konum Bulma", "red"))


ip = input("IP Adress: ")

response = requests.get("https://freeipapi.com/api/json/"+ ip)

data = response.json()


if response.status_code == 200:
   # print(data)
    print(colored("\n\n\n\nIP Adresi bulundu!", "green"))
    print(data["ipAddress"])
    print("Google Maps: \nhttps://www.google.com/maps/search/?api=1&query="+str(data["latitude"])+","+str(data["longitude"]))
    print("-"*5)
    print("Ülke: "+data["countryName"])
    print("Bölge: "+data["regionName"])
    print("Şehir: "+data["cityName"])
    print("-"*5)
    print("Zaman Dilimi: "+data["timeZone"])
    print("-----DETAYLI BİLGİLER-----\n")
    print("Proxy(?) "+str(data["isProxy"]))
    print("IP versiyonu: "+str(data["ipVersion"]))
