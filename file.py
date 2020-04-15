# -*-coding:utf-8 -*
import os
os.chdir("/home/patrice/Documents")


mon_fichier = open ("fichier.txt", "w")
contenu = mon_fichier.read()
print(contenu)
mon_fichier.close()