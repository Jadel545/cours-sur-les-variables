# exercice 1 : les string 

'''ecrit un programme qui demande à l'utilisateur:
-quel est ton nom
-donne moi ta ville 
-quel est ta couleur préférer'''

# nb:pour demander les informations à l'utlisateur ( entrer les informations) on utilise la fonction input()

# food=input("quel est ton plat préférer : ")
# print(f"votre nourriture préférer est {food}")

# nom=input("quel est ton nom : " )
# print(f"votre nom est {nom} ")
# ville=input("quel est ta ville : ")
# print(f"votre ville est {ville}")
# couleur=input("quel est ta couleur préférer : ")
# print(f"votre couleur préférer est {couleur}")

# print(f"votre nom est {nom} , vous habitez à {ville} et votre couleur préférer est {couleur}")

#Exercice 2: int
'''ecrit un programme qui demande à l'utilisateur:
-quel age as tu?
-combien y a t'il d'habitant dans ta maison ? 
-si l'age est inferieur à 18 on dira tu es enfant par contre ( sinon ) tu es jeune adulte
'''
age=int(input("quel est ton age (nombre entier): "))
print(f"votre age est {age} ans ")
habitant=int(input("combien y a t'il d'habitant dans ta maison (nombre entier): "))
print(f"il y a {habitant} habitants ")
print(f"votre age est {age} ans et vous êtes {habitant} habitants")


if age < 18:
    print("tu es enfant")
else:
    print("tu es jeune adulte")

    