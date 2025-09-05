# import random
# nombres=[2,12,19,73,6,2]
# noms=["jack","jean","mary","jeremy","adams","rose","beni","jean"]
# random.shuffle(nombres)
# print(nombres)
# nombres.append(45)
# random.shuffle(nombres)
# print(nombres)




# print("pour les nombres")
# print(nombres.count(2))
# nombres.reverse()
# print(nombres)
# nombres.sort()
# print(nombres)
# nombres.sort()
# print(nombres)
# nombres.pop()
# print(nombres)
# nombres.pop(2)
# print(nombres)
# print(nombres)
# print(len(nombres))
# print(nombres[4])
# print(nombres[len(nombres)-1])
# nombres.remove(19)
# print(nombres)
# nombres.clear()
# print(nombres)
# print(nombres[0])
# print(nombres[1])
# print(nombres[2])
# print(nombres[3])
# print(nombres[4])
# nombres.append(45)
# print(nombres)
# print(len(nombres))
# nombres.insert(0,78)
# print(nombres)
# print(len(nombres))
# nombres.extend([2,4,55,86,89])
# print(nombres[4])
# print(nombres[len(nombres)-1])
# print(nombres)
# print(len(nombres))

#print("pour les noms")
# print(noms)
# print(len(noms))
# print(noms[0])
# print(noms[1])
# print(noms[2])
# print(noms[3])
# noms.append("juda")
# print(noms)
# print(len(noms))
# noms.insert(2,"july")
# print(noms)
# print(len(noms))
# noms.extend(["celeste","rabi","john"])
# print(noms)
# print(len(noms))
# print(noms[len(noms)-1])
# noms.remove("jack")
# print(noms)
# noms.clear()
# print(noms)
# noms.sort()
# print(noms)
# noms.pop()
# print(noms)
# print(noms.count("jean"))
# noms.reverse()
# print(noms)
#print(noms.index("jean"))



#reponse 1
# limite=0
# liste=[]
# while limite<5:
#     fruit=input("veillez entrer le nom d'un fruit : ")
#     liste.append(fruit)
#     limite+=1
#     print(f"vous avez ajouter un fruit et la liste devient  {liste}")
# try:
#  fruit_suppr=input("quel fruit voulez vous supprimer : ")
#  liste.remove(fruit_suppr)
# except ValueError:
#    print("veillez supprimer le bon element")
# else:
#     print(f"voici votre liste de fruit {liste} ")
#     print(f"voici le premier fruit {liste[0]}")
#     print(f"voici le dernier fruit {liste[len(liste)-1]}")
#     print(f"voici la taille de votre liste {len(liste)}")

#reponse 2
# n=0
# paire=[2,4,26,8,10,15]
# impaire=[1,23,5,37,9,11]
# nombres=[]
# # nombres.extend(paire)
# nombres.extend(impaire)
# nombres=paire+impaire
# print(nombres)
# nombres.sort()
# print(nombres)
# nombres.pop()
# print(nombres)
# for i in nombres:
#     if i==nombres[len(nombres)-1]:
#         nombres.remove(i)
#         print(nombres)

# reponse 3
# liste=[21,4,-65,8,10,124]
# for i in liste :
#     if i<0:
#         print(f"{i} est négatif donc ERROR")
#     else:
#         print(f"{i} est positif")

#reponse 4
# temps=True
# liste=[]
# while temps:
#     try:
#         nbrs=int(input("veillez entrer un entier : "))
#         liste.append(nbrs)
#     except ValueError:
#         print(" entrer un entier et non des caractère ")
#     else:
#         stoP=input("voulez vous arreter si oui taper stop : ")
#         if stoP=="stop":
#          print(f"voici votre liste {liste} ")  
#          temps=False

#reponse 5
# try:
#     couleur=["rouge","vert","mate","violet","jaune","gris","bleu","indigo"]
#     renseigne=input("renseigner une couleur : ")
#     index=couleur.index(renseigne)
#     print(f"voici l'indice de cette couleur {index}")
# except ValueError:
#     print("cette couleur ne se trouve pas dans cette liste ")

#reponse 6
vide=[]
slicing=[1,3,4,5,7,8,10,12,13,14,16,17,19,21]
new=slicing[0:6]

for n in new:
    try:
        if n in slicing:
            slicing.remove(n)
    except:
        print("ERROR")
        print(f"nouvelle liste {slicing}")
print(slicing)
# for i in slicing:

#     for g in new:
#         # print(i)
#         if g==i:
#             slicing.remove(i)
#             vide.append(i)
#             print(vide)
          
# if new in slicing:
#     print(slicing)
# for i in new:
#     print(i)
#     if i==:
#         slicing.remove(i)
#         print(slicing)
# print(len(slicing)/2)
# print(slicing[5:9])
# # slicing.pop()
# # slicing.pop()
# # slicing.pop()
# # slicing.pop()
# # slicing.extend([30,40,71,52])
# slicing[10:14]=[30,40,71,52]
# print(slicing)

# print(slicing)
# slice=[10,12,13,14]
# print(slice)
# slicing.pop()
# slicing.pop()
# slicing.pop()
# slicing.pop()
# slicing.extend([30,40,71,52])
# print(slicing)
# nombres=[2,4,6,8,10,12,14,16,18,20]
# print(nombres[4:5])
    


