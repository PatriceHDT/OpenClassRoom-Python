# -*-coding:utf-8 -*
import os

from pend_fonctions import *
from pend_donnees import max_essai

# let_a_trouv = 0
partie = 'O'
nom = input("Bonjour, quel est votre nom ? ")

try:
    nom = str(nom)
    nom = nom.strip()
    nom = nom.lower()
    nom = nom.capitalize()
except:
    print("désolé je n'ai pas compris votre nom")

score = recup_score(nom)

print ("{0}, vous avez actuellement {1} points.".format(nom, score))


while input("Souhaitez vous faire une nouvelle partie ? (O/N) ").upper() == 'O':
    # mystere = choix_mot()
    lettres_essayees=[]
    mystere = "BAGUETTE"
    mot_affiche=cache_mot(mystere)[0]
    let_a_trouv=cache_mot(mystere)[1]
    essai = 0
    print ("vous devez trouver quel mot se cache sous {0}, il vous reste {1} lettres à trouver".format("".join(mot_affiche),let_a_trouv))

    
    while (let_a_trouv > 0) and (essai < max_essai):
        lettre = recup_lettre()
        if  lettre in lettres_essayees:
            print("Vous avez déja essayée la lettre {0}".format(lettre))
            recup_lettre()
        lettres_essayees.append(lettre)
        
        mot_affiche = cherche_lettre(mystere,lettre,mot_affiche,let_a_trouv,essai)[0]
        let_a_trouv = cherche_lettre(mystere,lettre,mot_affiche,let_a_trouv,essai)[1]
        essai = cherche_lettre(mystere,lettre,mot_affiche,let_a_trouv,essai)[2]
        if let_a_trouv == 0:
            print("Gagné, vous avez trouvé {0} en {1} essais".format("".join(mot_affiche),str(essai)))
            score +=1
            ecrit_score(nom,score)
        elif essai == max_essai:
            print("Perdu, il vous restait {0} lettres à trouver pour découvrir le mot {1}".format(let_a_trouv,mystere))
            score -=1
            ecrit_score(nom,score)
        else :
            print("Il vous reste à trouver {0} lettres en {2} essais, pour trouver quel mot se cache sous {1}".format(let_a_trouv,"".join(mot_affiche),str(max_essai-essai)))
            
    
