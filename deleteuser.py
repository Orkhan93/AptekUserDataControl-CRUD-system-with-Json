import json

def getDataFromToFile(_fileName):
    with open(_fileName,"r") as connect:
        return json.load(connect)
data=getDataFromToFile("database.json")

def getFromDataUser():
    u_name=input("Silmek istediyiniz User adini daxil edin : ")
    u_password=int(input("Silmek istediyiniz User parolunu daxil edin : "))
    for i in data['users']:
        if i['name']==u_name and i['password']==u_password:
            data['users'].pop(data['users'].index(i))
            print(f"{i['name']} adli istifadecinin butun melumatlari silindi")
    with open("database.json","w") as connect:
        json.dump(data,connect)

getFromDataUser()
