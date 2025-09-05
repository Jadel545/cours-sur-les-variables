#reponse 1

# livre={
#     "titre":"python facile",
#     "auteur":"samy",
#     "page":250
# }
# print(livre["titre"])

# #reponse 2
# livre["page"]=300
# livre.pop("auteur")
# print(livre)

# #reponse 3
# note={
#     "alice":15,
#     "bob":12,
#     "clara":18
#}
# for nom,note in note.items():
#     print(f"votre nom est {nom} et vous avez obtenu {note}/20")

#reponse 4
# keys=input("veillez entrer la clé coorespondante : ")
# print(note.get(f"{keys}","clé inexistante"))

#reponse 5
# employer={
#     "001":{
#         "nom":"clara",
#         "poste":"comptable",
#         "salaire":500000
#     },
#     "002":{
#         "nom":"mike",
#         "poste":"directeur technique",
#         "salaire":800000
#     }
# }
# print(employer["002"]["nom"])
# salaire=((500000*10)/100)+500000
# employer["001"]["salaire"]=salaire
# print(employer["001"]["salaire"])
# for i in employer.values():
#     print(i["nom"])
    
#reponse 6
vente={
    "janvier":12000,
    "mars":9500,
    "février":14000,
    "septembre":25000,
    "avril":10000,
    "octobre":30000
}
ordre=sorted(
#prend les items(d'un dictionnaire)
vente.items(),
#prend la clé (lambda)
key=lambda
#prend items (on prend les valeurs du dictionnaire)
item:item[1],
#pour avoir une liste croissante (true decroissante)
reverse=False
)
# print(ordre)
for mois,somme in ordre:
    print(f"le chiffre d'affaire du mois de {mois} est {somme}")
# vente(sorted)


#reponse 7
# phrase=input("veillez entrer une phrase : ")
# mini=phrase.lower()
# for i in mini:
#     if i!=" ":
#         nbrs=mini.count(i)
#         print(f"la phrase {phrase} est composé de {nbrs} : {i}")   

#devoir 1
# valeur=0
# produit=[("pomme",50,250),("lait",10,7000),("pain",500,100),("poisson",3,2000)]
# for article,quantité,prix in produit:
#     total=quantité*prix
#     valeur+=total
#     print(f"{article} a pour total {total}")
#     if quantité<=3:
#         print(f"Attention stock faible pour {article}")
# print(f"la valeur total du stocke est {valeur} ")

#devoir 2
# somme=0
# dic={}
# limite=1
# while limite <=3:
#     nom=input(f"veillez entrer le nom {limite}: ")
#     try:
#         note=float(input(f"veillez entrer la note {limite} : "))
#         somme+=note
#         limite+=1 
#     except ValueError:
#         print("entrer une note valide")
#     dic.setdefault(nom,note)
#     for n,o in dic.items():
#         print(f"{n} a obtenu {o}")
#         if o>=10:
#             print("vous etes admis")
#         else:
#             print("vous etes echouer")
# limite-=1
# moyenne=somme/limite
# print(f"la classe a une moyenne de {moyenne} ")
# print(dic)
    
#devoir 3
# liste=[]
# dic={}
# nbrs_eleve=0
# somme=0
# sum=0
# nbrs_eleve=int(input("combien d'élève avez vous : "))
# limite=1
# while limite<=nbrs_eleve:
#     nom_eleve=input("entrer le nom de l'eleve : ")
#     limite+=1
#     lim=1
#     while lim<=3:
#         note=float(input(f"veillez entrer la note {lim} : "))
#         liste.append(note)
            
#         dic.setdefault(nom_eleve,liste)
        
#         lim+=1
#         print(dic)
# lim-=1
# for nom,liste_note in dic.items():
#     print(liste_note)
# moyenne=somme/lim
# sum+=moyenne
# if moyenne>=10:
#     print(f"{nom}: moyenne = {moyenne} -> admis")
# else:
#     print(f"{nom}: moyenne = {moyenne} -> echouer")
# print("stat finale")
# print(f"vous avez un total de {nbrs_eleve} élève")
# moyenne_general=sum/nbrs_eleve
# print(f"vous avez une moyenne générale de {moyenne_general}")





               
               
        

    
    