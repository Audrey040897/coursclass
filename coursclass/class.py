class Voiture:
    caractere = 0
    def __init__(self,m,c,v):
        self.marque = m
        self.couleur = c
        self.vitesse = v
        Voiture.caractere += 1
        
    def rouler(self):
        print(self.vitesse) 


print(Voiture.caractere)

v1 = Voiture("peugeot","rouge",14)

print(Voiture.caractere)

v2 = Voiture("renault","bleu",25)

print(Voiture.caractere)

v1.rouler()
v2.rouler()
class Personne:
    def __init__(self,nom,prenom,couleur,date_naissance):
        self._nom = nom
        self.prenom = prenom
        self.couleur= couleur
        self.date_naissance = date_naissance
        
    def se_deplacer(self):
        return "en_marchant" 

    @property
    def age(self):
        return 2021 - self.__date_naissance

    def __str__(self):
        return f"{self._nom} {self.prenom}" 
    
    @property
    def date_naissance(self):
        return self.__date_naissance
    
    @date_naissance.setter
    def date_naissance(self,annee):
        print('Verification')
        self.__date_naissance = annee

p1 = Personne("lokoh","Audrey","noir",2010)

print(p1.se_deplacer())
print(p1.age)
print(p1.date_naissance)
p1.date_naissance = 2020
print(p1.date_naissance)