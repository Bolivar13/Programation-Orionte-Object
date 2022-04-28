import re
s = input("saisir un titre :")
x= re.search(r"\b[a-z]",s)
if x :
    print("ok")
else :
    print("ko")



#km