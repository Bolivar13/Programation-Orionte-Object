from abc import ABC


class Composition(ABC):
    def __init__(self,produit,quantité):
        self.__produit =produit
        self.__quantité =quantité

    @property
    def get_produit(self):
       f"{self.__produit}"

    def str_produit(self,value):
        f"{self.__produit}"
    
    @property
    def get_quantité(self):
       f"{self.__quantité}"

    def str_quantité(self,value):
        f"{self.__quantité}"


class Produit(ABC):
   def __init__(self,nom,code):
       self.__nom = nom
       self.__code = code

   @property
   def get_nom(self):
        f"{self.__nom}"

   def get_code(self):
        f"{self.__code}"

   @classmethod
   def getPrixHt(self):
       return self.getPrixHt


class Produit_élémentaire(Produit):

    def __init__(self,prixAchat,nom,code):
        self.__prixAchat =prixAchat
        super().__init__(self,nom,code)

    @staticmethod

    def __str__(self):
        return self.__prixAchat

    @classmethod
    def getPrixHT(self):
        return self.__prixAchat


class Produit_composé(Produit):
    tauxTVA =0.18
    def __init__(self,fraisFabrication,listeContituants,nom,code):
        self.__fraisFabrication = fraisFabrication
        self.__listeContituants = listeContituants 
        super().__init__(self,nom,code)

    @property
    def get_fraisFabrication(self):
        f"{self.__fraisFabrication}"

    def get_listeContituants(self):
        f"{self.__listeContituants}"
 
    @staticmethod
    def __str__(self):
        return   self.__fraisFabrication 

    @staticmethod
    def __str__(self):
        return self.listeContituants

    @classmethod
    def  getPrixHT(self):
       c= self.getPrixHT*self.tauxTVA
       print('le prix hors taxe et',c)
       return c  

    
   # p1,ps2
    #p3=2*ps1+4*p2
    #p4=3*p2+p1*2
p1 = Composition(Produit(10),2)
p1 = Composition(Produit(5),3)
p3 = Produit()