import json

def getDataFromToFile(_fileName):
    with open(_fileName,"r") as connect:
        return json.load(connect)

data=getDataFromToFile("database.json")


def getUserByPassword(_userPassword):
    for i in data['users']:
        if i['password']==userPassword:
            print(f"{i['name']} | {i['number']} | {i['mail']} | {i['username']}")

userPassword=int(input("Istifadeci kodunuzu daxil edin : "))
getUserByPassword(userPassword)


def getUserByName(_name):
    for i in data['users']:
        if i['name']==name:
            print(f"{i['name']} |  {i['number']} | {i['mail']} | {i['username']}")

name=input("Ad daxil ederek melumatla tanis olun : ")
getUserByName(name)


def getAptekByPassword(aptekPassword):
    for i in data['aptek']:
        if i['password']==aptekPassword:
            print(f"{i['name']} | {i['number']} | {i['mail']} | {i['username']}")

aptekPassword=int(input("Aptek istifadeci kodunu daxil edin : "))
getAptekByPassword(aptekPassword)

def getAptekByName(aptekName):
    for i in data['aptek']:
        if i['name'] == aptekName:
            print(f"{i['name']} | {i['number']} | {i['mail']} | {i['username']}")

aptekName=input("Aptek adini daxil ederek melumatlari alin : ")
getAptekByName(aptekName)



