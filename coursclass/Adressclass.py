class Adresse:
    def __init__(self,rue,ville,code_postal):
        self.__rue = rue
        self.__ville = ville
        self.__code_postal = code_postal
    
    @property
    def rue(sef):
        return self.__rue
    
    @rue.setter
    def rue(self,R):
        self.__rue = R
        
    @property
    def ville(self):
        return self.__ville
    
    @ville.setter
    def ville(self,V):
        self.__ville = V  

    @property
    def code_postal(self):
        return self.__code_postal
    
    @code_postal.setter
    def code_postal(self,c):
        self.__code_postal = c
        
        
    def __repr__(self):
        return f"{self.__rue} {self.__ville} {self.__code_postal}"