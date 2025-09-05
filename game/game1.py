#créer un jeu de devinette de nombre entre 1 et 10 
'''
ecrit manuellement le nombre à deviner 
demande à l'utilisateur entrer un nombre entre 1 et 10
nombre d'essai maximum 3
utilise un condition if pour comparer les reponses ( plus grand, plus petit, egal)
après chaque essaie à la fin annonce le resultat ( vous avez gagné ou vous avez perdu)'''
# import random
# nombre_a_devine=random.randint(1,10)
# print(nombre_a_devine)
# essai1=int(input("veillez entre un nombre entre 1 et 10 : "))
# if essai1>nombre_a_devine:
#     print(f"{essai1 } est plus grand")
#     print(f"le nombre a trouver etait {nombre_a_devine} ")
# elif essai1<nombre_a_devine:
#     print(f"{essai1} est plus petit")
#     print(f"le nombre a trouver etait {nombre_a_devine} ")
# else:
#     print(f"{essai1} est egal à {essai1}")
#     print("vous avez gagné")


'''
pour acceder à une conference l'utilisateur saisit son age et le montant d'argent qu'il possède:
l'entrer cout 1500 fca 
si l'age est inferieur à 18 ans l'entrer est refusé et aucun cadeau n'est possible
si l'utilisateur à plus de 18 ans il peut entrer seulement si sans montant est >= à 1500 fca
lorsqu'il accede à la conference 
moins de 25 ans il reçoit 500 fca et entre 25 et 40 ans il reçoit 300 fca 
plus 40 ans reçoit 250 fca
si l'utilisateur a au moins 60 ans , on lui retire 500 fca '''

age_utisateur=int(input("veillez entrer votre age : "))
montant=int(input("veillez entrer le montant que vous possédez : "))
solde=1500
if age_utisateur >=18:
    if montant>=solde:
       nouveauSolde=montant-solde
       print(f"vous pouvez entrer , vous avez payé {solde} votre nouveau solde est {nouveauSolde}")
       if age_utisateur<25:
          nouveau_Solde=nouveauSolde + 500
          print(f"vous recevez 500 fca et votre nouveau solde est {nouveau_Solde}")
       elif age_utisateur>=25 and age_utisateur<=40:
             newSolde=nouveauSolde + 300
             print(f"vous recevez 300 fca et votre nouveau solde est de {newSolde}")
       elif age_utisateur>40 and age_utisateur<60:
             new_solde=nouveauSolde + 250
             print(f"vous recevez 250 fca et votre solde est de {new_solde}")
       elif age_utisateur>=60 : 
             nMontant=nouveauSolde - 500
             print(f"on vous retire 500 , votre solde est à présent de {nMontant}")
       else:
           print("vous n'avez pas accès  age")
    else:
       print("vous avez pas accès")
else:
    print("accès refusé")

    



















# if age_utisateur<18:
#     print("vous ne pouvez pas entrer car vous n'avez pas l'age requis")
#     print(f"aucun cadeau n'est possible à {age_utisateur} ans ")
# elif age_utisateur>18 and montant>=entrer:
#     print(f"tu peut entrer car tu as {age_utisateur} et que tu as {montant}")
#     if age_utisateur<25:
#         print("vous recevez 500 fca")
#     elif age_utisateur>25 and age_utisateur<40:
#         print("vous recevez 300 fca")
#     elif age_utisateur>40:
#         print("vous recevez 250 fca")
#     else:
#         print("on vous retire 500 fca")
# else:
#     print("vous ne pouvez pas entrer")


