class Compte():
    def __init__(self, num, solde):
        self.num = num
        self.__solde = solde


    def get_solde (self):
        print("Lecture du solde")
        return self.__solde
         
    def set_solde (self, value):
        if value >= 0:
            print("Modification du solde")
            self.__solde= value
        else:
            print("Impossible")

    def del_solde(self):
        print("Delete solde")
    
     






















