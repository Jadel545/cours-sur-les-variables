
# n1=float(input("veillez entrer n1 : "))
# n2=float(input("veillez entrer n2 : "))
# somme=n1+n2
# print(f"la somme de {n1} et {n2} est {somme}")
# difference=n1-n2
# print(f"la difference entre {n1} et {n2} est {difference}")
# produit=n1*n2
# print(f"le produit de {n1} et {n2} est {produit}")
# quotient=n1/n2
# print(f"le quotient de {n1} et {n2} est {quotient}")
# reste=n1%n2
# print(f"le reste entre {n1} et {n2} est {reste}")

# def demande_option():
#     print("**************************")
#     print()
#     print("Pour calculer taper : ")
#     print("1 - pour l'addition")
#     print("2 - pour la difference")
#     print("3 - pour le produit")
#     print("4 - pour le quotient")
#     print("pour quitter taper : (quit) ou (stop) ou encore (q)")
#     print()
#     print("***************************")

# def somme(a,b):
#    return a+b

# def difference(a,b):
#     return a-b

# def produit(a,b):
#     return a*b

# def quotient(a,b):
#     return a/b

# def nbr1():
#     nbr1=float(input("entrer un premier nombre : "))
#     return nbr1

# def nbr2():
#     nbr2=float(input("entrer le deuxieme nombre : "))
#     return nbr2

# def operation():
#     temps=True
#     while temps:
#         demande_option()
#         operateur=input("quel operateur sohaitez vous utiliser : ")
#         if operateur=="1":
#             print(somme(nbr1(),nbr2()))
#         elif operateur=="2":
#             print(difference(nbr1(),nbr2()))
#         elif operateur=="3":
#             print(produit(nbr1(),nbr2()))
#         elif operateur=="4":
#             print(quotient(nbr1(),nbr2()))
#         else:
#             demande_option()
#         quitter=input("pour quitter taper : (quit) ou (stop) ou encore (q) : ")
#         if quitter=="q" or quitter=="quit" or quitter=="stop":
#             print("fin du programme")
#             temps=False

# operation()


# temps=True
# while temps

# bibliotheque = {
#     1: {"titre": "1984", "auteur": "George Orwell", "disponible": True},
#     2: {"titre": "L'Étranger", "auteur": "Albert Camus", "disponible": False},
#     3: {"titre": "Le Petit Prince", "auteur": "Antoine de Saint-Exupéry", "disponible": True}
# }
    
# def demande_option():
#     print("**************************")
#     print()
#     print(" menu ")
#     print("taper 1 - pour ajouter un livre")
#     print("taper 2 - pour rechercher un livre")
#     print("taper 3 - pour emprunter un livre")
#     print("taper 4 - pour rendre un livre")
#     print("taper 5 - pour afficher")
#     print("taper 6 - pour arrêter le programme")
#     print()
#     print("***************************")

# demande_option()

# tape=int(input("veillez entre votre proposition : "))



# def ajouter_livre():
#     dic={}
#     if tape==1:
#         limite=1
#         while limite<=3:
#             reference=input("entrer les references : ")
#             if reference=="titre":
#                 ref=input("veillez entrer le titre du livre que vous comptiez ajouter : ")
#             elif reference=="auteur":
#                 ref=input("veillez entrer l'auteur du livre que vous comptiez ajouter : ")
#             elif reference=="disponibilité":
#                 ref=bool(input("veillez entrer la disponibilité du livre que vous comptiez ajouter : "))
#             dic.setdefault(reference,ref)
#             limite+=1
#         bibliotheque.setdefault(4,dic)
#         print(bibliotheque)

# def recherche_livre():
#     if tape==2:
#             recherche=input("quel livre cherchez vous (veillez y entrer le titre) : ")
#             for nbrs,dic1 in bibliotheque.items():
#                 if recherche==dic1["titre"]:
#                     print(dic1.get)
                


# def emprunte_livre():
#     if tape==3:
#         emprunte=input("quel livre sohaitez vous emprunter (veillez entrer le titre) : ")
#         for nbrs,dic2 in bibliotheque.items():
#             if emprunte==dic2["titre"]:
#                 if dic2["disponible"]==False:
#                     print("nous avons pas ce livre en stocke")
#                     break
#                 else:
#                     dic2["disponible"]= not dic2["disponible"]
#                     print(dic2)    


# def rendre_livre():
#     if tape==4:
#         emprunte=input("quel livre sohaitez vous emprunter (veillez entrer le titre) : ")
#         for nbrs,dic2 in bibliotheque.items():
#             if emprunte==dic2["titre"]:
#                 if dic2["disponible"]==True:
#                     print("ce livre n'a jamais été emprunter")
#                     break
#                 else:
#                     dic2["disponible"]= not dic2["disponible"]
#                     print(dic2)    


# def afficher_livre():
#     if tape==5:
#         return bibliotheque

# ajouter_livre()
# recherche_livre()
# emprunte_livre()
# rendre_livre()
# print(afficher_livre())
    
    
    
    
  