#exercice 1
'''
crée un programme compte à rebour de 10 à 1 avec la boucle white

exercice 2
affiche les nombres paires  de 0 à  20 avec for et continue

exercice 3 
affiche un carré d'etoile 5*5 avec des boucle inbriquer

exercice 4

demande à l'utlisateur combien de note il veut saisir(nombre entier)
pour chaque note demande la saisi (nombre flottant) entre 0 et 20 
vérifie que la note est valide entre 0 et 20
si la note est invalide redemande la
calcule la moyenne des note valide
affiche la moyenne final avec un message selon la note 
si la moyenne est superieur ou egale à 10 affiche admit*
sinon affiche ajourné'''

#reponse 1

# compte_a_rebour=10
# while compte_a_rebour>0:
#     print(f"compte a rebour:{compte_a_rebour}")
#     compte_a_rebour-=1

#reponse 2

# for i in range(0,21):
#     if i%2!=0:
#         continue
#     print(i)
    
#reponse 3
# for i in range(0,5):
#     for n in range(0,5):
#         print("*",end="")
        
    

#reponse 4
# nbrs_de_note=int(input("combien de note voulez vous entrer : "))
# print(f"vous voulez saisir {nbrs_de_note} notes")
# limite=1
# somme=0
# while limite<=nbrs_de_note:
#     notes=float(input(f"veillez entre la note {limite} (nombre à virgule) : "))
#     print(f"vous avez saisi {notes}")
#     if notes>=0 and notes<=20:
#         print("votre note se trouve bien entre 0 et 20")
#         limite+=1
#         somme+=notes
#     else:
#         print(f"la note {notes} n'est pas valide")
#     moyenne=somme/nbrs_de_note
# print(f"vous avez une moyenne de {moyenne}")
# if moyenne>=10:
#     print(f"avez une moyenne de {moyenne} vous etes admit")
# else:
#     print(f"avec une moyenne de {moyenne} vous etes ajourné")


'''
exercice 5
saisi l'heure (entier) entre 0 et 23 puis affiche 
de 0 à 11 bonjour , debut de matiné
de 12 à 17 bonne après midi 
de 18 à 21 h bon soir
de 22 à 5h bonne nuit '''
# attente=True
# while attente:
#     heure=int(input("veillez entrer l'heure actuel : "))
#     if heure>=0 and heure<=11:
#         print("bonjour,debut de matiné")
#     elif heure>=12 and heure<=17:
#         print("bonne après midi")
#     elif heure>=18 and heure<=21:
#         print("bon soir")
#     else:
#         print("bonne nuit")
#     quit=input("voulez vous quitter la boucle ? taper (q ou quitter) : ")
#     if quit=="q" or quit=="quitter":
#         attente=False
#         print("fin du programme")

# prix=10000 
# taux=50/100
# calcule=prix*taux
# print(calcule)

# prix=10000 
# taux=0.5
# calcule=prix*taux
# print(calcule)

# nom=input("entrer votre nom : ")
# print(nom)
# print(nom.upper())
# print(len(nom))
# majuscule=any(m.isnumeric() for m in nom)
# print(majuscule)
# miniscule=any(n.islower for n in nom)
# print(miniscule)
    
 


#exercice 1

'''demande à l'utilisateur un mot de passe et verifie s'il contient
au moins 8 caractère
une majuscule
un chiffre
affiche mot de passe securisé
ou liste les manquant
tand que la condition est vrai 

exercice 2 
calculateur de reduction
l'utilisateur saisi un prix et une categorie
etudiant 30%
enseignant 20% et parents 10%
affiche le prix finale'''



# reponse 1


# limite=True
# while limite:
#     try:
#         password=str(input("veillez entrer un password : "))
#     except ValueError:
#         print("votre mot de passe doit contenir au moins 8 caractère , au moins une majuscule et un chiffre ")
#     else:
#         majuscule=any(i.isupper() for i in password)
#         chiffre=any(m.isnumeric() for m in password)
#         nbrs_de_caractere=len(password)
#         if nbrs_de_caractere >=8 and majuscule and chiffre:
#             print("votre mot de passe est valide")
#             print(f"{password}")
#             break     
#         else:
#             print("mot de passe invalide")
#             if nbrs_de_caractere<8:
#              print("votre password doit contenir au moins 8 caractères ")
#             if not majuscule:
#              print("votre password doit contenir au moins une majuscule")
#             if not chiffre:
#              print("votre password doit contenir au moins un chiffre") 
            

#reponse 2

temps=True
while temps:
    try:
        prix=float(input("veillez entrer le prix : "))
    except ValueError or TypeError:
        print("veillez entrer un float")
    else:
        categories=["etudiant","enseignant","parent"]
        for nom in categories:
            print(f"pour la categorie {nom} ")
        categorie=input("veillez entrer une catégorie : ")
        etudiant=0.3
        enseignant=0.2
        parents=0.1
        if categorie=="etudiant":
            final=prix-(etudiant*prix)
            print(f"le prix final est de {final}")
        elif categorie=="enseignant":
            final=prix-(enseignant*prix)
            print(f"le prix final est de {final}")
        elif categorie=="parents":
            final=prix-(parents*prix)
            print(f"le prix final est de {final}")
        else:
            print("veillez entrer une categorie valide s'il vous plait")
            
    


# try:
#     taille=int(input("veillez entrer votre taille : "))
#     print(taille)
# except ValueError:
#       print("erreur")

# try:
#     x=5/0
#     print(x)
# except ZeroDivisionError:
#     print("on ne peut pas divisé par 0")
# else:
#     print(f"la reponse est {x} ")
# finally:
#     print("fin du programme")
    
    
        



        




