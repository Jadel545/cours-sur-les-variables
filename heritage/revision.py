class telephone:
    def __init__(self,nom):
        self.nom=nom
    def marque(self):
        return"ce telephone est soit un samsung ou un apple"
    def version(self):
        return"obcelète"


class android(telephone):
    def __init__(self, nom,modele,date_sortie):
        self.modele=modele
        self.date=date_sortie
        super().__init__(nom)
    def marque(self):
        return f"ce telephone est un {self.nom} {self.modele} sortie le {self.date}"
    def fabriquant(self):
        return"la corée"

mon_phone=android("samsung","A15","10/09/2023")
print(mon_phone.marque())
print(mon_phone.fabriquant())
print(mon_phone.version())

