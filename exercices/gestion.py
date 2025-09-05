temps=True
while temps:
    try:
        nbrs_eleve=int(input("combien d'élève avez vous : "))
        dic={}
        liste3=[]
        eleve=[]
        classe={}
        limite=1
        moyenne_t=0
        while limite<=nbrs_eleve:
            nom_eleve=input(f"veillez entrer le nom de l'élève {limite} : ")
            lim=1
            liste2=[]
            while lim<=3:
                lite1=[]
                try:
                    note_eleve=float(input(f"entrer la note {lim} : "))
                    if lim==1:
                        note1=note_eleve
                    if lim==2:
                        note2=note_eleve
                    if lim==3:
                        note3=note_eleve
                        print(f"{note1}, {note2} et {note3}")
                    lite1.append(note_eleve) 
                except ValueError:
                    print("entrer une note valide")
                else:
                    lim+=1  
                for element in lite1:
                    liste2.insert(0,element)  
            dic.setdefault(nom_eleve,liste2)
            limite+=1
            lim-=1
            liste3.extend([liste2])
            print(liste3)
            somme=0
            print(dic.items())
            for i in liste2:
                somme+=i
            liste4=[]
            moyenne=somme/lim
            moyenne_t+=moyenne
            liste4.append(moyenne)
            classe.setdefault(nom_eleve,moyenne)
            print(classe)
            if moyenne>=10:
                print(f"{nom_eleve} : Moyenne = {moyenne} → Admis")
            else:
                print(f"{nom_eleve} : Moyenne = {moyenne} → échouer")
        print("stats finales")
        print(f"vous avez un total de {nbrs_eleve}")
        moyenne_g=moyenne_t/nbrs_eleve
        print(f"cette classe à une moyenne de {moyenne_g}")
        classement=sorted(
        classe.items(),
        key=lambda
        item:item[1],
        reverse=True
        )
        nbrs=1
        for nom,moy in classement:
            print(f"le numero {nbrs} est {nom} avec une moyenne de {moy}")
            nbrs+=1
        break
    except ValueError:
        print("veillez entrer une valeur valide")