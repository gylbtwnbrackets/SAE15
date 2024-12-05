#Exercice 1
def lire_fichier(fichier : str) -> str :
    with open(fichier, "r", encoding="UTF-8") as mon_fichier :
        contenu = mon_fichier.read()
    return contenu 

def ecrire_fichier(fichier : str, chaine : str) -> str :
    with open(fichier, "w") as mon_fichier :
        mon_fichier.write(chaine)

#Exercice 2
assoc= dict[str,str]
def decode_entete(fichier: str) -> assoc:
    paires = {}
    with open(fichier, "r", encoding="UTF-8") as mon_fichier :
        header = mon_fichier.read()
    for i in range(len(header),3)  :
            if header[i] == "+" :
                paires[header[i+1]] = header[i+2]
    return paires 

def cherche_corps(fichier: str) -> str:
    with open(fichier, "r", encoding="UTF-8") as mon_fichier :
        whole = mon_fichier.read()
    head = ""
    sliced = []
    for i in range(len(whole)) :
        if whole[i] != ".":
            head += whole[i]
        elif whole[i] == ".":
            sliced.append(head)
            head = ""
    sliced.append(head)
    return sliced[1]

def decode_corps(fichier : str) -> str :

            
        
    
    

