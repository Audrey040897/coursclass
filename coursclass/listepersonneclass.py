
class ListePersonnes:
    def __init__(self,personnes = []):
        self.__personnes = personnes
    
    @property
    def personnes(self):
        return self.__personnes
    
    @personnes.setter
    def personnes(self,p):
        self.__personnes = p
        
    def __repr__(self):
        return f"{self.personnes}"    

    def find_by_nom(self,s:str):
        for personne in self.personnes:
            if personne.nom == s:    
                return personne

    def exists_code_postal(self,cp):
        for personne in self.personnes:
            for adresse in personne.adresses:
                if adresse.code_postal == cp:
                    return True
                else:
                    return False
    
    def count_personne_ville(self, ville):
        count = 0
        for personne in self.personnes:
            for adresse in personne.adresses:
                if ville == adresse.ville:
                    count += 1
                    break
            continue
        return count
    
    def edit_personne_nom(self,oldNom,newNom):
        for personne in self.personnes:
            if personne.nom == oldNom:
                personne.nom = newNom
                
    def edit_personne_ville(self,nom,newville):
        for personne in self.personnes:
            for adresse in personne.adresses:
                if nom == adresse.ville:
                    adresse.ville= newville
    
    def __getitem__(self,index):
        return self.personnes[index]
    
    def __setitem__(self,index ,value):
        self.personnes[index] = value
    
    def __delitem__(self,index):
        del self.personnes[index]   