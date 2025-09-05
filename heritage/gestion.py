class personne:
    def __init__(self,nom,age):
        self.nom=nom
        self.age=age
    def affiche_info(self):
        print(f"Nom: {self.nom} , âge: {self.age}")

  
class eleve(personne):
    def __init__(self, nom, age,classe,notes):
        self.classe=classe
        self.notes=notes
        super().__init__(nom, age)
    def ajouter_notes(self,matiere,note):
        self.dit={}
        limite=1
        while limite<=4:  
            matiere=input("quelle est la matière correspondante : ")
            note=float(input("quelle est la note correspondante : "))
            self.dit.setdefault(matiere,note)
            print(self.dit)
            limite+=1
    def calcule_moyenne(self):
        for m,n in self.dit.items():
            m=0
            somme=0
            m+=1
            somme+=n
            moyenne=somme/m
            print(moyenne)

class professeur(personne):
    def __init__(self, nom, age,matiere_enseigne):
        self.matiere_enseigne=matiere_enseigne
        super().__init__(nom, age)
    def affiche_info(self):
        print(f"nom: {self.nom}, âge: {self.age} et matière enseignée: {self.matiere_enseigne}")

dico_eleves = {}

dico_profs = {}

matieres = ["Mathématiques", "Physique", "Français", "Histoire"]

limte=True
i=1
while limte:
    nom_eleve=input("entrer le nom de l'élève : ")
    age_eleve=int(input("entrer l'âge de cet élève : "))
    classe=input("quel est la classe de cette élève : ")
    mon_eleve=eleve(nom_eleve,age_eleve,classe,"")
    dico_eleves.setdefault(i,mon_eleve)

    nom_prof=input("entrer le nom du prof : ")
    age_prof=int(input("entrer l'âge du prof : "))
    mat=input("quel matière enseigne se prof : ")
    if mat=="Mathématiques" or mat=="Physique" or mat=="Français" or mat=="Histoire":
        mon_prof=professeur(nom_prof,age_prof,mat)
        dico_profs.setdefault(i,mon_prof)
    else:
        print("cette matiere n'est pas dans le programme")    
    i+=1
    for a,b in dico_eleves.items():
        print(b.affiche_info())

    for c,d in dico_profs.items():
        print(d.affiche_info())
    
    ID_eleve=int(input("entrer l'ID de l'élève : "))
    objet=dico_eleves[ID_eleve]
    print(objet)
    objet.ajouter_notes("math",18)
    print(objet.calcule_moyenne())



    
    



    '''
Projet : Gestion d’une École (Élèves & Professeurs)
🎯 Objectif

Créer un mini-système qui permet de gérer une école. Tu vas modéliser des élèves et des professeurs avec des classes, stocker les données dans des dictionnaires et listes, et faire interagir tout ça avec des menus et des boucles.

📌 Cahier des charges
🟦 1. Classes

Classe Personne (classe parent)

Attributs : nom, age

Méthode : afficher_infos()

Classe Eleve (hérite de Personne)

Attributs supplémentaires : classe, notes (dictionnaire matière → note)

Méthodes :

ajouter_note(matiere, note)

calculer_moyenne()

Classe Professeur (hérite de Personne)

Attributs supplémentaires : matiere enseignée

Méthode : afficher_infos() (spécifique, qui indique la matière enseignée)

🟦 2. Structures de données

Un dictionnaire pour stocker tous les élèves, clé = identifiant, valeur = objet Eleve.

Un dictionnaire pour stocker tous les professeurs.

Une liste pour stocker les matières disponibles.

🟦 3. Menu principal (boucle infinie)

Ajouter un élève

Ajouter un professeur

Afficher tous les élèves

Afficher tous les professeurs

Ajouter une note à un élève

Calculer la moyenne d’un élève

Quitter

🟦 4. Gestion des erreurs (try/except)

Si l’utilisateur entre un texte au lieu d’un nombre (âge, note) → gérer avec try/except.

Si on demande un élève qui n’existe pas dans le dictionnaire → KeyError.

Si on tape un choix de menu invalide → afficher un message.

🟦 5. Exemple de scénario

Ajout d’un élève : Nom = Aiko, Âge = 15, Classe = 3A

Ajout d’un professeur : Nom = Mr. Tanaka, Âge = 40, Matière = Mathématiques

Affichage des élèves :

[1] Aiko, 15 ans, Classe : 3A, Notes : {}


Ajout d’une note : Aiko, Mathématiques = 14

Calcul de la moyenne :

Moyenne d’Aiko = 14.0

🚀 Points clés que tu vas travailler

Variables → identifiants, notes, moyennes, etc.

Listes → matières, notes d’un élève.

Boucles → menu principal.

Dictionnaires → gestion des élèves/professeurs.

Try/Except → sécuriser les entrées utilisateur.

Classes & Héritage → réutilisation de la classe Personne pour Eleve et Professeur.'''