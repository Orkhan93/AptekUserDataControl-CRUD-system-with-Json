import json

def getDataFromToFile(_fileName):
    with open(_fileName,"r") as connect:
        return json.load(connect)
data=getDataFromToFile("database.json")

def getDataFromAptek():
    a_name=input("Melumatlarini Silmek istediyiniz Aptekin adini daxil edin : ")
    a_password=int(input("Melumatlarini Silmek istediyiniz Aptekin parolunu daxil edin : "))
    for i in data['aptek']:
        if i['name']==a_name and i['password']==a_password:
            data['aptek'].pop(data['aptek'].index(i))
            print(f"{i['name']} adli aptekin butun melumatlari silindi")
    with open("database.json",'w') as connect:
        json.dump(data,connect)

getDataFromAptek()
