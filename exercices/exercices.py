'''
Exercice 1:
Création et accès
Crée un dictionnaire livre avec :  
- titre = "Python Facile"  
- auteur = "Samy"  
- pages = 250  
Puis affiche uniquement le titre.

Exercice 2:
 Mise à jour et suppression
À partir de livre, change le nombre de pages à 300 et supprime la clé "auteur".

Exercice 3:
Parcours
Crée un dictionnaire notes = {"Alice": 15, "Bob": 12, "Clara": 18}  
Affiche chaque nom avec sa notes

Exercice 4 :
Clé inexistante
Demande une clé à l’utilisateur et affiche la valeur correspondante, sinon affiche "Clé introuvable".
Voici 3 exercices plus avancés sur les dictionnaires Python, avec des cas réels :

---

Exercice 5:
 Dictionnaire imbriqué
Crée un dictionnaire employes contenant 2 employés avec leurs infos :  
python
{
  "e001": {"nom": "Ali", "poste": "Comptable", "salaire": 400000},
  "e002": {"nom": "Sarah", "poste": "Dev", "salaire": 600000}
}

1. Affiche le nom de e002  
2. Augmente le salaire de e001 de 10%  
3. Affiche tous les employés


Exercice 6 – Trier les valeurs
À partir du dictionnaire :
python
ventes = {"janvier": 12000, "mars": 9500, "février": 14000}

Trie les mois par chiffre d'affaires croissant et affiche-les.


Exercice 7:
Fréquence des lettres
Demande à l’utilisateur une phrase et affiche combien de fois chaque lettre apparaît. Ignore les espaces et rends tout en minuscule.

Devoir 1:
Tu veux gérer un petit stock de produits.  
1. Crée une liste de tuples, chaque tuple représentant un produit : (nom, quantité, prix_unitaire)  
2. Parcours la liste pour :
   - Afficher chaque produit avec son total (quantité × prix)  
   - Si la quantité est ≤ 3, affiche un message : « Attention stock faible pour [nom] »
3. Calcule et affiche la valeur totale du stock.

Devoir 2:
1. Demande à l’utilisateur d’entrer le nom et la note de 3 élèves (via input())  
2. Stocke ces infos dans un dictionnaire {nom: note}  
3. Parcours le dictionnaire pour :
   - Afficher : « [Nom] a obtenu [note] »  
   - Si note ≥ 10 : « Admis » ; sinon : « Échoué »  
4. Affiche la moyenne de la classe.

Devoir 3: Mini système de gestion scolaire

Tu dois développer un petit programme pour gérer des élèves d’une classe.

Étapes :

1. Ajout des élèves:  
   Demande à l’utilisateur combien d’élèves il veut enregistrer.  
   Pour chaque élève :
   - Saisie du nom
   - Saisie de 3 notes (sur 20)
   - Stocke les infos dans un dictionnaire:  
     {"nom": (note1, note2, note3)}
2. Calcul des moyennes :
   - Parcours le dictionnaire
   - Calcule la moyenne de chaque élève
   - Affiche « [Nom] : Moyenne = X → Admis/Échoué »
3. Statistiques finales :
   - Nombre total d’élèves
   - Moyenne générale de la classe
   - Élève avec la meilleure moyenne
'''

