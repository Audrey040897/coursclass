
class Personne:
    def __init__(self,nom,sexe,adresses = []):
        self.__nom = nom
        self.__sexe = sexe
        self.__adresses = adresses
        
    @property
    def nom(self):
        return self.__nom
    
    @nom.setter
    def nom(self,name):
        self.__nom  = name
    
    @property
    def sexe(self):
        return self.__sexe
    
    @sexe.setter
    def sexe(self,s):
        self.__sexe = s
    
    @property
    def adresses(self):
        return self.__adresses
    
    @adresses.setter
    def adresses(self,A):
        self.__adresses = A
    
    def __repr__(self):
        return f"{self.__nom} {self.__sexe} {self.__adresses}"
    
    def __getitem__(self,index):
            return self.adresses[index]
    
    def __setitem__(self,index ,value):
        self.adresses[index] = value
    
    def __delitem__(self,index):
        del self.adresses[index]    