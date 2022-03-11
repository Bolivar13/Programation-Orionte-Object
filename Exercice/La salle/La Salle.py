class salle():
    max_chaises=30
    max_tables= 20
    def __init__(self ,chaises, tables, tableux , projecteurs ):
        self.__nb.chaises = chaises
        self.__.tables= tables
        self.nb.tableux= tableux
        self.has.projecteur= projecteurs

    def set_nb_chaises(self , value):
        if value >=0 and value <=salle.max_chaises:
            self.__nb.chaises=value
            return self.__nb.chaises

    def set_nb_tables(self, value):
        if value >=0 and value <=salle.max_tables:
            self.__nb.tables=value
            return self.__nb.tables

    def ajouter_chaises(self,value):
        total = self.__nb.chaises+ value
        return self.set_nb_chaises(self.__nb.chaises + value)

    def supprimer_chaines(self, value):
        total = self.__nb_chaines - value
        return self.set_nb_chaises(self.__nb.chaises - value)

    def ajouter_tables(self,value):
        total = self.__nb.tables+ value
        return self.set_nb_tables(self.__nb.tables + value)

    def supprimer_tables(self, value):
        total = self.__nb_tables - value
        return self.set_nb_tables(self.__nb.tables - value)



salle_1 = ( 26 , 14 , 1 , 1 )
x = salle_1.ajouter_tables(1)
y = salle_1.ajouter_chaise(1)

print(x)
print(y)



















