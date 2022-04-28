import re


def valider_cin(s ):
#analise 
    x=re.search("^[A-Z]{3,6} [0 ,9] { 3 , 6}$", s)
    return True if x else False
    
print(valider_cin("JF1542361"))
     


 



