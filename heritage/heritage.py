# class animal:
#     def parler(self):
#         print("l'animal peut parler")

# # loup=animal()
# # print(loup.parler())

# class chien(animal):
#     def aboyer(self):
#         print("le chien aboy")

# mon_chien=chien()
# print(mon_chien.parler())
# print(mon_chien.aboyer())


# class lion(animal):
#     def rugi(self):
#         print("le lion rugi")

# mon_lion=lion()
# print(mon_lion.rugi())
# print(mon_lion.parler())

class animal:
    def __init__(self,nom):
        self.nom=nom

class chat(animal):
    def __init__(self, nom,couleur):
        self.couleur=couleur
        super().__init__(nom)
    def affiche_nom(self):
        return f"ce chat est appelé {self.nom}"
    def affiche_couleur(self):
        return f"ce chat est de couleur {self.couleur}"
        
    

mon_chat=chat("lion","noir")
print(mon_chat.affiche_nom())
print(mon_chat.affiche_couleur())


        



