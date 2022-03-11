class salle():

    max_chaises=30
    max_tables= 20

    def __init__(self ,chaises, tables, tableux , projecteurs ):
        self.__nb.chaises = chaises
        self.__.tables= tables
        self.nb.tableux= tableux
        self.has.projecteur= projecteurs
   #Chaises:

    @property   #getter (wajiha kharijia d attribut prive)
    def nb_chaises(self):
        return self.__nb_chaises

    @nb_chaises.setter
    def nb_chaises(self, value):
        if value >=0 and value <= salle.max_chaises :
         self.__nb_chaises =value

   
  
   #tables :

    @property  #getter
    def nb_tables(self):
        return self.__nb_tables

    @nb_tables.setter
    def nb_tables(self, value):
        if value >=0 and value <= salle.max_tables :
         self.__nb_tables =value

  
 
     

    
























