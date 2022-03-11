class Salle():

    max_chaises = 30
    max_tables = 20

    def __init__(self, chaises=0, tables=0, tableaux=0, proj=0):
        self.__nb_chaises = chaises
        self.__nb_tables = tables
        self.__nb_tableaux = tableaux
        self.__has_projecteur = proj

    def set_nb_chaises(self, value):
        if value >= 0 and value <= Salle.max_chaises:
            self.__nbr_chaises = value
            return self.__nbr_chaises

    def set_nb_tables(self, value):
        if value >= 0 and value <= Salle.max_tables:
            self.__nbr_tables = value
            return value

    def ajouter_chaises(self, value):
        return self.set_nb_chaises(self.__nb_chaises + value)

    def supprimer_chaises(self, value):
        return self.set_nb_chaises(self.__nb_chaises - value)

    def ajouter_tables(self, value):
        return self.set_nb_tables(self.__nb_chaises + value)

    def supprimer_tables(self, value):
        return self.set_nb_tables(self.__nb_chaises - value)


salle_1 = Salle(24)
salle_2 = Salle(1)
print(salle_2.ajouter_chaises(4))
print(salle_2.ajouter_tables(1))
