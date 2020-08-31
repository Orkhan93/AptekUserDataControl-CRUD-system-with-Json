import json

def getDataFromToFile(_fileName):
    with open(_fileName,"r") as connect:
        return json.load(connect)

data=getDataFromToFile("database.json")

def getFromDataUser():
    userName=input("Melumatlarini deyismek istediyiniz User adini daxil edin : ")
    userPassword=int(input("Melumatlarini deyismek istediyiniz User parolunu daxil edin : "))
    name=input("Yeni ad daxil edin : ")
    number=int(input("Yeni nomre daxil edin : "))
    mail=input("Yeni mail adresi daxil edin : ")
    username=input("Yeni username daxil edin : ")
    password=int(input("Yeni sifre daxil edin  : "))
    for i in data['users']:
        if i['username']==userName and i['password']==userPassword:
            i['name']=name
            i['number']=number
            i['mail']=mail
            i['username']=username
            i['password']=password
            print(f"{i['name']} adli istifadecinin butun melumatlari yenilendi")
    with open("database.json","w") as connect:
        json.dump(data,connect)

getFromDataUser()
