class compte():
    def __init__(self,num,nom):
        self.num=num
        self.nom=nom
        self.__sold=0
    def get_sold(self):
        return self.__sold
    def crediter(self,s):
        self.__sold -=s
        return self.__sold
    def debiter(self,s):
        self.__sold+=s
        return self.__sold
    def afficher(self):
        print(f"compte: {self.num}")
        print(f"nom : {self.nom}")
        print(f"sold: {self.__sold}")
f1=compte("12","Simon")
print(f1.nom, f1.num, f1.afficher(), f1.debiter(100))
print(f1.afficher())

















