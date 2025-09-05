# tuple=("jean",19,True)
# print(f"je m'appel {tuple[0]} et j'ai {tuple[1]} ans , je suis etudiant {tuple[len(tuple)-1]}")
# tuple=(11,2,3,2,9,7,2,3)
# print(tuple.count(3))
# print(tuple.index(7))


'''
crée un tuple nommé voiture contenant les information suivantes
marque: "toyota" 
modele: "corola"
année: 2020
puis affiche la marque et l'année'''

# voiture=("toyota","corola", 2020)
# print(f"la marque de la voiture est {voiture[0]} de l'année {voiture[len(voiture)-1]}")


'''
crée une liste de trois etudiants en utilisant le tuple pour chaque etudinant
affiche le nom du deuxieme etudiant
modifie le nom du premier
supprime le nom du dernier
affiche la liste finale'''

# eleve=[("fred",12),("july",15),("anna",0.5)]
# print(eleve[1][0])
# eleve.pop(0)
# eleve.insert(0,("john",15))
# eleve.pop()
# print(eleve)

#exercice 3
'''
parcourir une liste de tuple
tu dispose une liste :
'''

produits=[("pain",500),("lait",350),("riz",800)]
produits[0]=("mangue",150)
produits[2]=()
print(produits)
'''affiche tous les produits sous la forme
Produit: Pain | prix:500'''

# Produits=[("pain",500),("lait",350),("riz",800)]
# for m in Produits:
#     print(f"produit: {m[0]} | prix: {m[1]}")

# trouver=False
# article=input("veillez entrer le nom de votre produit : ")
# for nom,prix in produits:
#     if nom.lower()==article.lower():
#         print(f"produit trouvé : {nom} avec {prix}")
#         trouver=True
#         break
# if not trouver:
#  print("Produit non trouver")
  
        
    

    
