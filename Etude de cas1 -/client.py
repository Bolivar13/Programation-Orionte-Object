import json
from  pathlib import Path
import re

class Client :
    filepath = "./Bibliothèque/data/clients.json"

    def __init__(self,nom,email,telephone,cin) -> None:
        self.__nom = nom
        self.__email = email
        self.__telephone = telephone
        self.__cin = cin 
        if Path(Client.filepath).exists():
            print(' found')
        else:
            print("not found,create it")
            with open(Client.filepath,'w') as f:
                f.write('[]')

#---------------------------------------------------------
    @property
    def get_nom(self):
        return self.__nom

    def set_nom(self,nom):
        self.__nom = nom

#---------------------------------------------------------
    @property
    def get_email(self):
        return self.__email

    def set_email(self,email):
        self.__email = email

#---------------------------------------------------------
    @property
    def get_telephone(self):
        return self.__telephone

    def set_telephone(self,telephone):
        self.__telephone = telephone

#---------------------------------------------------------
    @property
    def get_cin(self):
        return self.__cin

    def set_cin(self,cin):
        self.__cin = cin

# ------------- la methodes str-----------------------------

    def str(self):
        return f"le nom :{self.__nom}\nemail :{self.__email}\nphone :{self.__telephone}\ncin :{self.__cin}"
    
        
    def sauvegarder(self):
        data = {
                "name" : self.__nom , 
                "gmail" : self.__email,
                "phone" : self.__telephone,
                "cin" : self.__cin
            }   
        with open(Client.filepath,"r") as f:
            print('reading file')
            clients = json.loads(f.read())
            print(' file loaded')
            print(clients)
            clients.append(data)
        with open(Client.filepath , "w") as f:
            f.write(json.dumps(clients))    
        

def chercher(value):
    with open(Client.filepath , "r") as f :
        clients = json.loads(f.read())
        for c in clients:
            n = c["name"]
            x = re.findall(f"^{value}",n)
    return Client(
            c["name"],
            c["gmail"],
            c["phone"],
            c["cin"]
        )
            

if __name__ == '__main__':
    cl = Client("mohamed","mohamed@gmail.com","0655555555","JF65093")
    cl.sauvegarder()
    cl2 = Client("ali","mohamed@gmail.com","0655555555","JF65093")
    cl2.sauvegarder()
    cl3 = Client("ahmed","mohamed@gmail.com","0655555555","JF65093")
    cl3.sauvegarder()
    cl4 = Client("khalid","mohamed@gmail.com","0655555555","JF65093")
    cl4.sauvegarder()
    chercher("khalid")