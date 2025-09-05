'''
crée une classe livre avec les attributs titre et auteur
methode :
presentation() qui retourne "le livre(titre) a ete ecrit par l'auteur (auteur)

exercice2
crée une classe etudiant avec nom , prenon et age 
methodes:
presentation() if l'etudiant a moins de 18 ans tu es mineur sinon tu es majeur'''


#reponse 1
# class livre:
#     def __init__(self,titre,auteur):
#         self.titre=titre
#         self.auteur=auteur
#     def presentation(self):
#         return f"ce livre a pour titre {self.titre} et pour auteur {self.auteur}"
    
# objet=livre("L'Etranger","jean")
# print(objet.presentation())
# objet2=livre("harry","mary")
# print(objet2.presentation())

#reponse 2
# class etudiant:
#     def __init__(self,nom,prenom,age):
#         self.nom=nom
#         self.prenom=prenom
#         self.age=age
#     def presentation(self):
#         return f"cette etudiant s'appele {self.nom} {self.prenom} et a {self.age} ans"
#     def verification(self):
#         if self.age<18:
#             print("tu es mineur")
#         else:
#             print("tu es jeune adulte")
    
# objet=etudiant("jack","ngaga",18)
# print(objet.presentation())
# print(objet.verification())
# objet2=etudiant("jonathan","poaty",12)
# print(objet2.presentation())
# print(objet2.verification())
# objet3=etudiant("","kim",20)
# print(objet3.presentation())
# print(objet3.verification())

# class salutation:
#     def __init__(self):
#         pass
#     def dire_bonjours(self):
#         return"bonjour"
#     def temps(self):
#         heure=13
#         if heure<12:
#             print("c'est le matin")
#         elif heure==12:
#             print("il est midi")
#         else:
#             print("c'est le soir")

# salut=salutation()
# print(salut.dire_bonjours())
# print(salut.temps())


'''
crée un classe compte pour simuler un compte bancaire simple avec
titulaire
solde
des methode pour depot,retrait,afficher le solde'''

temps=True
class compte:
    def __init__(self,titulaire,solde):
        self.titulaire=titulaire
        self.solde=solde
    def choix(self,option):
        option=input("que voulez vous faire (un depot , un retrait ou afficher le solde) : ")
        if option!="depot" and option!="retrait" and option!="afficher le solde":
            print("entrer l'une de nos propositions")
    def depot(self,option):
        if option=="depot":
            if self.solde>0:
                try:
                    montant=float(input("veillez entrer la somme du depot : "))
                    if montant>0:
                        print(montant)
                        self.solde +=montant
                        print(f"votre solde est de {self.solde} fcfa")
                    else:
                        print("vous ne pouvez pas faire un depot ")
                except ValueError:
                    print("entrer la somme correcte")
            else:
                print("vous ne pouvez pas faire de depot")
    def retrait(self,option):
        if option=="retrait":
            try:
                retrait=float(input("veillez entrer la somme à retirer : "))
                print(retrait)
                if retrait<=self.solde:
                    if retrait>=100:
                        self.solde-=retrait
                        print(f"votre solde est de {self.solde} fcfa")
                    else:
                        print("vous ne pouvez que retirer 100 ou plus ")
                else: 
                    print(f"vous ne pouvez pas retirer cette somme car votre solde est de {self.solde} fcfa")
            except ValueError:
                print("entrer la somme correcte")
    def affiche_solde(self,option):
        if option=="afficher le solde":
            return f"le solde de {self.titulaire} est de {self.solde} fcfa"
        

sujet=compte("james",5000)
temps=True
while temps:
    print(sujet.choix())
    print(sujet.depot())
    print(sujet.retrait())
    print(sujet.affiche_solde())
    q=input("voulez vous arrêter si oui taper stop : ")
    if q=="stop":
        print("fin du programme")
        temps=False
