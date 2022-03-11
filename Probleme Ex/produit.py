from abc import ABC

class Composition(ABC):
    def __init__(self,produit, quantite):
        self.__produit =produit
        self.__quantite =quantite

    @property     
    def get_produit(self , __produit ):
       return self.__produit
      
    def str_produit(self, __produit):  
        return self.__produit
    
    @property   
    def get_quantite(self):
       return self.__quantite

     
    def str_quantité(self,quantite):
        return self.__quantite


class produit(ABC):
   def __init__(self,nom,code):
       self.__nom = nom
       self.__code = code

   @property      
   def get_nom(self):
        return self.__nom

     
   def get_code(self):
     return self.__code 

 



        
 