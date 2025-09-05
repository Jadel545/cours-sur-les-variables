'''
Projet : Mini Bibliothèque Numérique
🎯 Objectif

Créer un programme qui permet de gérer une bibliothèque simple :

Ajouter des livres avec leur titre, auteur, et disponibilité.

Rechercher un livre par titre ou auteur.

Emprunter ou rendre un livre (changer son état de disponibilité).

Afficher tous les livres de la bibliothèque.

Utiliser try/except pour gérer les erreurs de saisie.

Organiser le code en fonctions.

📌 Cahier des charges détaillé
🟦 1. Structure de données

Un dictionnaire pour stocker les livres :

bibliotheque = {
    1: {"titre": "1984", "auteur": "George Orwell", "disponible": True},
    2: {"titre": "L'Étranger", "auteur": "Albert Camus", "disponible": False},
    3: {"titre": "Le Petit Prince", "auteur": "Antoine de Saint-Exupéry", "disponible": True}
}


👉 La clé = un identifiant unique du livre.
👉 La valeur = un dictionnaire avec infos.

🟦 2. Menu principal (boucle)

Le programme propose :

Ajouter un livre

Rechercher un livre (par titre ou auteur)

Emprunter un livre

Rendre un livre

Afficher tous les livres

Quitter

🟦 3. Variables principales

bibliotheque → dictionnaire des livres.

id_livre → variable pour donner un identifiant unique aux nouveaux livres.

🟦 4. Fonctions à créer

ajouter_livre(bibliotheque, id_livre, titre, auteur)
➝ ajoute un nouveau livre.

rechercher_livre(bibliotheque, mot_clef)
➝ affiche tous les livres qui contiennent ce mot dans le titre ou l’auteur.

emprunter_livre(bibliotheque, id_livre)
➝ marque le livre comme non disponible.

rendre_livre(bibliotheque, id_livre)
➝ marque le livre comme disponible.

afficher_bibliotheque(bibliotheque)
➝ affiche tous les livres avec leur état.

🟦 5. Gestion des erreurs

Si on tape un ID de livre qui n’existe pas → afficher un message.

Si on essaie d’emprunter un livre déjà emprunté → avertir l’utilisateur.

Si on tape une mauvaise valeur (ex. lettre au lieu d’un nombre) → try/except pour éviter le crash.

🚀 Exemple de scénario d’utilisation (en langage naturel)

L’utilisateur lance le programme → menu.

Il choisit 1 → ajoute : "Harry Potter", "J.K. Rowling".

Il choisit 5 → affiche :

[1] 1984 - George Orwell (Disponible)
[2] L'Étranger - Albert Camus (Emprunté)
[3] Le Petit Prince - Antoine de Saint-Exupéry (Disponible)
[4] Harry Potter - J.K. Rowling (Disponible)


Il choisit 3 → emprunter [4] Harry Potter.

Il choisit 5 → affiche que Harry Potter est Emprunté.

Il choisit 6 → programme terminé.'''

bibliotheque = {
    1: {"titre": "1984", "auteur": "George Orwell", "disponible": True},
    2: {"titre": "L'Étranger", "auteur": "Albert Camus", "disponible": False},
    3: {"titre": "Le Petit Prince", "auteur": "Antoine de Saint-Exupéry", "disponible": True}
}

recherche=input("quel livre cherchez vous (veillez y entrer le titre) : ")
for nbrs,dic1 in bibliotheque.items():
    if recherche==dic1["titre"]:
        print(dic1)