print("beinvenue chez joueur dans deviné le nombre")
nbrs=7
essai1=int(input("veillez entrer un nombre entre 1 et 10  : "))
if essai1>nbrs :
    print(f"{essai1} est plus grand")
elif essai1==nbrs:
    print(f"{essai1} est égal à {nbrs}")
    print("vous avez gagné")
else:
    print(f"{essai1} est plus petit")
essai2=int(input("veillez entrer votre essai2  : "))  
if essai2>nbrs :
    print(f"{essai2} est plus grand")
elif essai2==nbrs:
    print(f"{essai2} est égal à {nbrs}")
    print("vous avez gagné")
else:
    print(f"{essai2} est plus petit")
essai3=int(input("veillez entrer votre essai3  : "))  
if essai3>nbrs :
    print(f"{essai3} est plus grand")
    print("vous avez perdu")
elif essai3==nbrs:
    print(f"{essai3} est égal à {nbrs}")
    print("vous avez gagné")
else:
    print(f"{essai3} est plus petit")
    print("vous avez perdu")
