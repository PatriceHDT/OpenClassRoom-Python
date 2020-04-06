# -*-coding:utf-8 -*
import os

"""
# Mettre en minuscule une chaîne de caractères
chaine = "NE CRIE PAS SI FORT !"
print (chaine.lower())
"""

chaine = str()

while chaine.lower() != "q":
    print("Tapez 'Q' pour quitter...")
    chaine = input()
    print(chaine)

print("Merci !")

