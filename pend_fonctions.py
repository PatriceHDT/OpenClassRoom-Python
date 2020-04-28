
# -*-coding:utf-8 -*

''' Liste des fonctions du jeu de pendu

demander le nom du joueur
initialiser le score du joueur si c'est sa première fois
choisir un mot au hazard dans la liste
demander une lettre au joueur
vérifier si la lettre est dans le mot
afficher le mot avec les lettres découvertes
compter les essais
enregistrer le score
'''

import os
import random
import pickle

from pend_donnees import *

print(__doc__)
print(mots)

def choix_mot():
    ''' choisit un mot au hazard parmi la liste "mots"'''
    i = random.randint(1,len(mots))
    mot = mots[i]
    return (mot)


def init():
    '''vérifie l'existence du fichier score, charge les scores et si non existant créé le tout'''
    try:
         with open('pendu_scores','rb') as fichier:
            scores=pickle.Unpickler(fichier)
    except:
        with open('pendu_scores','wb') as fichier:
            scores={}
            mon_pickler = pickle.Pickler(fichier)
            mon_pickler.dump(scores)
    return(scores)

init()


def recup_score(joueur):
    score = scores[joueur]
    return (score)

print(recup_score('patrice'))

