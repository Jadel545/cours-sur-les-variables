nom="jack"
print(nom.upper())

#fonction sans parametre
# def dire_bonjour():
#     print("bonjours tous le monde")


# def hello_world():
#     return " hello world"

# def multiplication():
#     a=5
#     b=4
#     result=a*b
#     return result

# dire_bonjour()
# print(hello_world())    
# print(multiplication())

#fonction avec parametre
# def get_name():
#     name=input("entrer votre nom : ")
#     return f"vous avez saisi {name}"


# def get_age():
#     age=int(input("veillez entrer votre age : "))
#     return age

def affiche_info(nom,age):
    print(f"votre nom est {nom} et vous avez {age} ans ")
    if age <18:
        print("vous êtes mineur")
    else:
        print("vous êtes un jeune adulte")

affiche_info(get_name(),get_age())



# nom(name,age)
# vericateur_age(age)
# print(se_presenter("jack"))

def produit():
    return "mangue"

def prix():
    return 1000

# print(produit())
# print(prix())
produit()