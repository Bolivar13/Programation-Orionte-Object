import re


def valider_username(s):

    x=re.search("[a-zA-Z+0-9]+_" , s)
    if x :
        print("valide") 
    else  : 
        print("invalide")

s = input ("Enter Username:")     

print(valider_username(""))
     
