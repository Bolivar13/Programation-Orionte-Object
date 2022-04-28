import re


s = input ("Enter Username:")     

x=re.search("[a-zA-Z [0-9] _",s)
if x :
    print("valide") 
else  : 
    print("invalide")


