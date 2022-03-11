from multiprocessing.sharedctypes import Value


class vehicule():
  def __init__(self , matricule , marque, anne_circulation, prix_jour ) :
    self.__matricule = matricule
    self.__marque= marque
    self.__anne_circulation = anne_circulation
    self.__prix_jour = prix_jour
 
 



  @property 
  def __matricule(self):
    return  self.__matricule

  @__matricule.setter
  def __matricule(self , value):
   self.__matricule = Value





@property
def __marque(self):
    return self.__marque
@__marque.setter
def __marque(self , value):
    self.__marque = value





@property
def anne_circulation(self):
    return self.anne_circulation
@anne_circulation.setter
def anne_circulation(self , value):
    self.anne_circulation = value

   
     
  


@property
def prix_jour(self):
    return self.prix_jour
@prix_jour.setter
def prix_jour(self , value):
    self.prix_jour = value
  
 