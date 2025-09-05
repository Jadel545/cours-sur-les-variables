'''
exercice 1
crée une classe vehicule avec une methode demarrer et une methode arrêter
puis la classe voiture qui herite de vehicule puis ajoute la methode klaxoner'''

# class vehicule:
#     def demarrer(self):
#         print("ce vehicule demarre")
#     def arreter(self):
#         print("ce véhicule est à l'arrêt")

# class voiture(vehicule):
#     def klaxoner(self):
#         print("ce véhicule klaxone")

# ma_voiture=voiture()
# print(ma_voiture.demarrer())
# print(ma_voiture.arreter())
# print(ma_voiture.klaxoner())

'''
exercice 2
crée une classe animal avec attribut nom ,
methode parler,affiche puis crée deux class chien et chat qui herite de l'animal et redefinis parler() pour le chien wouf et pour le chat miou'''

# class animal:
#     def __init__(self,nom):
#         self.nom=nom
#     def parler(self):
#         print("...")
    
# class chien(animal):
#     def __init__(self, nom):
#         super().__init__(nom)
#     def parler(self):
#         print(f"le {self.nom} abouy wouf")
    
# class chat(animal):
#     def __init__(self, nom):
#         super().__init__(nom)
#     def parler(self):
#         print(f"le {self.nom} miou")

# mon_chien=chien("gad")
# print(mon_chien.parler())
# mon_chat=chat("mimnou")
# print(mon_chat.parler())

'''
exercice 3
crée une class personne avec un attribut nom avec une methode se presenter()
qui affiche bonjour je m'appel {nom}
ensuit crée une class etudiant qu herite de personne
dans la class etudiant redefint la methode se presenter personnaliser de l'etudiant '''

# class personne:
#     def __init__(self,nom):
#         self.nom=nom
#     def se_presenter(self):
#         print(f"bonjour je m'appel {self.nom}")

# class etudiant(personne):
#     def __init__(self, nom,prenom,age):
#         self.prenom=prenom
#         self.age=age
#         super().__init__(nom)
#     def se_presenter(self):
#         print(f"je suis l'etudiant {self.nom} {self.prenom} et j'ai {self.age} ans")

# ma_presentation=etudiant("kevin","parckeur",24)
# sujet=personne("tony")
# print(ma_presentation.se_presenter())
# print(sujet.se_presenter()) 

'''
Exercice 4 : Formes géométriques

Crée une classe Forme avec une méthode aire() qui renvoie 0 par défaut.

Crée deux classes qui héritent de Forme :

Rectangle (avec largeur et hauteur, calcule l’aire).

Cercle (avec rayon, calcule l’aire).

Demande à l’utilisateur de choisir une forme, d’entrer les dimensions, et affiche l’aire correspondante.'''


'''
Exercice 5 : Système d’école

Crée une classe Personne avec les attributs nom et âge.

Crée une classe Étudiant qui hérite de Personne et ajoute niveau (classe de l’étudiant).

Crée une classe Professeur qui hérite de Personne et ajoute matière.

Demande à l’utilisateur de créer une liste mixte de professeurs et d’étudiants.

Parcours la liste et affiche pour chacun :

S’il s’agit d’un étudiant → "Je suis NOM j'ai AGE, étudiant en NIVEAU".

S’il s’agit d’un professeur → "Je suis NOM et j'ai AGE, je donne le cours de MATIÈRE".'''


#reponse 4

# class forme:
#     def __init__(self):
#         pass
#     def aire(self):
#         return 0

# class rectangle(forme):
#     def __init__(self):
#         super().__init__()
#     def aire(self):
#             self.a=float(input("entrer la largeur : "))
#             self.b=float(input("entrer la hauteur : "))
#             air=self.a*self.b
#             return air

# class cercle(forme):
#     def __init__(self):
#         super().__init__()
#     def aire(self):
#             self.r=float(input("entrer le rayon : "))
#             air=3.14*self.r**2
#             return air

# temps=True
# while temps:
#     choix=input("quel forme vouler vous (rectangle ou cercle): ")
#     if choix=="rectangle":
#         geo2=rectangle()
#         print(f"l'air de se rectangle est {geo2.aire()}")
#     if choix=="cercle":
#         geo3=cercle()
#         print(f" l'air de se cercle est {geo3.aire()}")
#     q=input("si vous avez terminé taper q : ")
#     if q=="q":
#         temps=False


# class personne:
#     def __init__(self,nom,age):
#         self.nom=nom
#         self.age=age
#     def affiche_info(self):
#         return f"je suis {self.nom} et j'ai {self.age}"

# class etudiant(personne):
#     def __init__(self, nom, age,classe_etudiant):
#         self.classe_etudiant=classe_etudiant
#         super().__init__(nom, age)
#     def affiche_info(self):
#         return f"Je suis {self.nom} et j'ai {self.age}, étudiant en {self.classe_etudiant}"

# class prof(personne):
#     def __init__(self, nom, age,matiere):
#         self.matiere=matiere
#         super().__init__(nom, age)
#     def affiche_info(self):
#         return f"Je suis {self.nom} et j'ai {self.age}, je donne le cours de {self.matiere}"

# liste=[]
# temps=True
# while temps:
#     nom_prof=input("entrer le nom du prof : ")
#     age_prof=int(input("entrer l'âge du prof : "))
#     matiere_enseigner=input("veillez y entrer la matière enseignée par le prof : ")
#     objet1=prof(nom_prof,age_prof,matiere_enseigner)
#     liste.append(objet1)

#     nom_etudiant=input("entrer nom de l'étudiant : ")
#     age_etudiant=int(input("enter l'âge de cette étudiant : "))
#     classe=input("entrer la classe correspondante de l'étudiant : ")
#     objet2=etudiant(nom_etudiant,age_etudiant,classe)
#     liste.append(objet2)

#     print(liste)

#     q=input("avez vous terminer si oui taper q : ")
#     if q=="q":
#         temps=False

# for i in liste:
#     print(i.affiche_info())


'''
exercice 6
crée un programme de todoList pour effectuer une operation CRUD en utilisant la POO 
 '''
dico={}
class produit:
    def __init__(self,nom,prix,isComplet):
        self.nom=nom
        self.prix=prix
        self.isComplet=isComplet
    def info(self):
        return f"le produit {self.nom} avec prix : {self.prix}"
    def creat(self):
        dico.setdefault(self.nom,self.prix)
        return""
    def read(self):
        return dico 
    
    
    
    # def update(self):
nom=input("veillez entrer le nom de votre produit : ")
prix=float(input("veillez entrer le prix de votre produit : "))
objet=produit(nom,prix,False) 

# print(obje",18000,Falseet1.info())
# print(objet2.info())
# print(objet.creat())
objet.creat()
print(objet.read())
        
