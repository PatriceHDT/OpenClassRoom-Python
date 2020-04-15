# -*-coding:utf-8 -*
import os
import pickle
os.chdir("/home/patrice/Documents")

# 
# mon_fichier = open ("fichier.txt", "r")
# contenu = mon_fichier.read()
# print(contenu)
# mon_fichier.close()
# 


# # lecture ecriture fichier texte
# with open("fichier.text", "a") as mon_fichier:
#     mon_fichier.write("Une ligne de plus dans mon fichier")

# with open("fichier.txt" , "r") as mon_fichier:
#     contenu = mon_fichier.read()
#     print(contenu)


score = {
    "joueur 1": 5,
    "Joueur 2": 20,
    "Joueur 3": 35,
    "Joueur 5": 18
}

with open("donnee", "wb") as fichier:
    mon_pickler = pickle.Pickler(fichier)
    mon_pickler.dump(score)

with open("donnee" , 'rb') as fichier:
    mon_dePlicker = pickle.Unpickler(fichier)
    score_recupere = mon_dePlicker.load()
    print(score_recupere)
