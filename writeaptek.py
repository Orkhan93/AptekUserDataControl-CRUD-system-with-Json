import json

def getDataFromToFile(_fileName):
    with open(_fileName,"r") as connect:
        return json.load(connect)

data=getDataFromToFile("database.json")
def getDataFromAptek():
    print("Yeni yaradilacaq olan Aptekin melumatlarini daxil edin")
    a_name=input("Aptek adini daxil edin : ")
    a_number=int(input("Aptekin elaqe nomresini daxil edin : "))
    a_mail=input("Aptekin Mail adresini daxil edin : ")
    a_username=input("Istifadeci adinizi daxil edin : ")
    a_password=int(input("Istifadeci Kodunuzu daxil edin : "))
    print(f"{a_name} adli yeni Aptek sisteme elave edildi")
    aptek={
        "name": a_name,
        "number": a_number,
        "mail": a_mail,
        "username": a_username,
        "password": a_password
    }
    data['aptek'].append(aptek)
    with open("database.json","w") as connect:
        json.dump(data,connect)


getDataFromAptek()
