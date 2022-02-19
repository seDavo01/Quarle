# Pour ajouter + de mots, où je me suis arrêté : https://motsavec.fr/5-lettres/dictionnaire/mots-courants/20


#Fonction pour retirer les accents
import unicodedata
def remove_accents(text):
    try:
        text = unicode(text, 'utf-8')
    except NameError: # unicode is a default on python 3 
        pass

    text = unicodedata.normalize('NFD', text)\
           .encode('ascii', 'ignore')\
           .decode("utf-8")

    return str(text)


#Tout remettre sur 1 seule ligne
f = open('listemots.txt', 'r')
lines = f.readlines()
listemots = '\t'.join([line.strip() for line in lines])
 
# On remplace les trois petits points
clean1 = listemots.replace("…", "")
# On retirer les accents
clean2 = remove_accents(clean1)
# Et on retirer les noms propres
temp = clean2.split()
nbMots = len(temp)
res = " ".join([ele for ele in temp if not ele[0].isupper()])
 
# printing result
print(str(res))
print("Total de " + str(nbMots) + " mots")