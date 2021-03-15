import personneclass, Adressclass, listepersonneclass

A1 = Adressclass.Adresse("cocody","abidjan",1346)
A2 = Adressclass.Adresse("angre","abidjan",7965)
p1 = personneclass.Personne("jean","M",[A1])
p2 = personneclass.Personne("brice","F",[A2])
p3 = personneclass.Personne("axel","M",[A1])
p4 = personneclass.Personne("axel","F",[A2])
lp = listepersonneclass.ListePersonnes([p1,p2,p3,p4])
print(lp.find_by_nom("jean"))
print(lp.exists_code_postal(1246))
print(lp.count_personne_ville("abidjan"))
lp.edit_personne_nom("axel", "boris")
print(p3)
print(p4)
lp.edit_personne_ville("abidjan","bouaké")
print(p1)
print(p2)
print(lp.personnes[1])
lp.personnes[0] = p2
print(lp)
del lp.personnes[2]
print(lp)
print(lp.personnes[2])
a =p1.adresses
print(a)