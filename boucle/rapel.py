# temps=True
# while temps:
#     try  :
#         prix=float(input("veillez entrer le prix : "))
#         categories=["etudiant","enseignant","parent"]
#         for nom in categories:
#             print(f"pour la categorie {nom} ")
#         categorie=input("veillez entrer une catégorie : ")
#         etudiant=0.3
#         enseignant=0.2
#         parents=0.1
#         if categorie=="etudiant":
#             final=prix-(etudiant*prix)
#         elif categorie=="enseignant":
#             final=prix-(enseignant*prix)
#         elif categorie=="parents":
#             final=prix-(parents*prix)
#         print(f"le prix final est de {final}")
#     except ValueError :
#         if prix:
#             print("veillez entrer un nombre")
#         if categorie:
#             print("veillez entrer une categorie valide")

        

# limite=True
# while limite:
#     try:
#         password=input("veillez entrer un password : ")
#         majuscule=any(i.isupper() for i in password)
#         chiffre=any(m.isnumeric() for m in password)
#         nbrs_de_caractere=len(password)
        
#         print("votre mot de passe est valide")
#         if nbrs_de_caractere <=8 and not majuscule and not chiffre:
#           print(f"{password}")
        
#         break     
#     except:
       
#         print("mot de passe valide")
#         if nbrs_de_caractere<8:
#            print("votre password doit contenir au moins 8 caractères ")
#         if not majuscule:
#            print("votre password doit contenir au moins une majuscule")
#         if not chiffre:
#            print("votre password doit contenir au moins un chiffre") 
        


# temps=True
# while temps:
#     try:
#         prix=float(input("veillez entrer le prix : "))
#         try:
#             categories=["etudiant","enseignant","parent"]
#             for nom in categories:
#                 print(f"pour la categorie {nom} ")
            
#             categorie=input("veillez entrer une catégorie : ")
#             etudiant=0.3
#             enseignant=0.2
#             parents=0.1
#             if categorie=="etudiant":
#                 final=prix-(etudiant*prix)
#                 print(f"le prix final est de {final}")
#             elif categorie=="enseignant":
#                 final=prix-(enseignant*prix)
#                 print(f"le prix final est de {final}")
#             elif categorie=="parents":
#                 final=prix-(parents*prix)
#                 print(f"le prix final est de {final}")
#         except ValueError:
#             print("veillez entrer une categorie valide")

#     except ValueError:
#         print("veillez entrer un nombre à virgule")
    
    
# temps=True
# while temps:
#     categories=["etudiant","enseignant","parent"]
#     for nom in categories:
#         print(f"pour la categorie {nom} ")
#         try:   
#             prix=float(input("veillez entrer le prix : "))
#         except ValueError:
#             print("veillez entrer un nombre")
#             try:
#                 categorie=input("veillez entrer une catégorie : ")
#             except ValueError:
#                 print("veillez entrer une categorie valide")
    
    
    
#     etudiant=0.3
#     enseignant=0.2
#     parents=0.1
#     if categorie=="etudiant":
#         final=prix-(etudiant*prix)
#         print(f"le prix final est de {final}")
#     elif categorie=="enseignant":
#         final=prix-(enseignant*prix)
#         print(f"le prix final est de {final}")
#     elif categorie=="parents":
#         final=prix-(parents*prix)
#         print(f"le prix final est de {final}")
#     else:
#         print("veillez entrer une categorie valide s'il vous plait")
        