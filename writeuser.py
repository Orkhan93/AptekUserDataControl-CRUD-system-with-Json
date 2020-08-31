import json

def getDataFromToFile(_fileName):
    with open(_fileName,"r") as connect:
        return json.load(connect)

data=getDataFromToFile("database.json")

def getDataFromUser():
    print("Yeni yaradilacaq profiliniz ucun melumatlari daxil edin")
    u_name=input("Adinizi daxil edin : ")
    u_number=int(input("Nomrenizi daxil edin : "))
    u_mail=input("Mail adresinizi daxil edin : ")
    u_username=input("Istifadeci adinizi daxil edin  : ")
    u_password=int(input("Istifadeci Kodunuzu daxil edin : "))
    print(f"{u_name} adli yeni User sisteme elave edildi")
    users ={
        "name": u_name,
        "number": u_number,
        "mail": u_mail,
        "username": u_username,
        "password": u_password
    }
    data['users'].append(users)
    with open("database.json","w") as connect:
        json.dump(data,connect)

getDataFromUser()

