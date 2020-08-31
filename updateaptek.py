import json

def getDataFromToFile(_fileName):
    with open(_fileName,"r") as connect:
        return json.load(connect)

data=getDataFromToFile("database.json")

def getFromDataAptek():
    aptekUsername=input("Melumatlarini deyismek istediyiniz aptekin istifadeci adini daxil edin : ")
    aptekPassword=int(input("Melumatlarini deyismek istediyiniz aptekin istifadeci parolunu daxil edin : "))
    name=input("Yeni ad daxil edin : ")
    mail=input("Yeni mail adresi daxil edin : ")
    username=input("Yeni username daxil edin : ")
    password=int(input("Yeni sifre daxil edin  : "))
    for i in data['aptek']:
        if i['username']==aptekUsername and i['password']==aptekPassword:
            i['name']=name
            i['mail']=mail
            i['username']=username
            i['password']=password
            print(f"{i['name']}adli Aptekin butun melumatlari yenilendi..")

    with open("database.json","w") as connect:
        json.dump(data,connect)

getFromDataAptek()
