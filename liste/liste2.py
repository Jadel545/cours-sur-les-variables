# import random
# chaine=[]
# chaine.extend(["jean","jack",True])
# chaine.append(10)
# chaine.insert(3,84.5)
# print(chaine)
# print(len(chaine))
# print(chaine[len(chaine)-1])
# produit=chaine[3]*chaine[4]
# random.shuffle(chaine)
# print(chaine)
# print(produit)

#reponse1
# temps=True
# liste=[]
# while temps:
#     article=input("veillez entrer le nom des articles que vous comptez acheter : ")
#     min=article.lower()
#     liste.append(min)
#     fin=input("avez vous fini (oui/non) : ")
#     if fin=="oui":
#       print("merci pour vos achat")
#       temps=False
#       print(f"voici votre liste {liste}")
# verification=input("voulez vous supprimer un article (oui/non): ")
# if verification=="oui":
#     try:
#         article_a_suppr=input("quel article voulez vous supprimer : ")
#         mini=article_a_suppr.lower()
#         if mini in liste:
#              liste.remove(mini)
#              print(f"voici votre liste {liste}")
#         else:
#             print("se nom ne se trouve pas dans la liste")
#     except ValueError:
#         print("veillez entrer le non de votre article ")
# else:       
#     print("merci pour vos achat")
#     temps=False

#reponse 2
# limite=1
# liste=[]
# temps=True
# while temps :
#     if limite>=2:
#         limite-=1
#     else:
#         try:
#             while limite <=2:  
#                 try:
#                     nbr=int(input(f"veillez entrer le {limite} nombre : "))
#                     if limite==1:
#                         nbr1=nbr
#                     if limite==2:
#                         nbr2=nbr
#                         print(f"{nbr1} et {nbr2}")
#                 except ValueError:
#                     print("ERREUR , entrer ce que nous vous demandions des entiers et operateurs")
#                 else:
#                     limite+=1
#             operateurs=input("quel operation souhaité exécuter (+, -, *, /) : ")  
#         except ValueError:
#             print("ERREUR , entrer ce que nous vous demandions des entiers ")
#         else:
#             if operateurs!="+" and operateurs!="-" and operateurs!="*" and operateurs!="/":
#                 print("ERREUR , veillez entrer un operateurs (+, -, *, /)")
#                 continue
#             elif operateurs=="+":
#                 operation=nbr1+nbr2
#             elif operateurs=="-":
#                 operation=nbr1-nbr2
#             elif operateurs=="*":
#                 operation=nbr1*nbr2
#             else:
#                 operation=nbr1/nbr2
#             print(f"le resultat est {operation}")
#             liste.append(f"{nbr1}{operateurs}{nbr2}={operation}")
#             quitter=input("avez vous terminer si oui taper stop  : ")
#             historique=input("voulez vous voir votre historique (oui/non) :")
#             if quitter=="stop":
#                 temps=False
#                 print("fin du programme")
#             if historique=="oui":
#                 print(f"historique : {liste}")
                

# #reponse 3
# liste=[]
# temps=True
# somme=0
# eleve=input("quel est votre nom : ")
# while temps:
#     try:
#         notes=float(input("veillez entrer une note : "))
#         somme+=notes
#         liste.append(notes)
#     except ValueError:
#         print("ERREUR , entrer que des float")
#     else:
#         fin=input("si vous avez terminé taper fin : ")
#         if fin=="fin":
#             temps=False
# moyenne=somme/len(liste)
# print(f"l'élève {eleve} a une moyenne de : {moyenne}")

#reponse 4
# import random
# hazard=random.randint(1,20)
# temps=True
# liste=[]
# print("devinez un nombre entre 1 et 20")
# while temps:
#     try:
#         nbrs_a_devine=int(input("veillez entrer un nombre : "))
#         liste.append(nbrs_a_devine)
#     except ValueError:
#         print("entrer que des nombres entiers")
#     else:
#         if nbrs_a_devine==hazard:
#             print(f"vous avez gagné le nombre à deviner était {hazard}")
#             print(f"liste d'essais {liste}")
#             temps=False


#reponse 5
# sites=[]
# passwords=[]
# limite=0
# while limite<5:
#     site=input("entrer un site : ")
#     sites.append(site)
#     password=input("entrer un mot de passe correspondant : ")
#     passwords.append(password)
#     limite+=1
# try:
#     nom_de_site=input("entrer un nom de site correspondant: ")
#     index=sites.index(nom_de_site)
#     mdp=passwords[index]
#     print(f"le mot de passe coorespondant est {mdp}")
# except IndexError:
#     print("veillez réessayer")

    
    









    
