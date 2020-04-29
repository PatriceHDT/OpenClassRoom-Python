
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
let_a_trouv = 0

def choix_mot():
    ''' choisit un mot au hazard parmi la liste "mots"'''
    i = random.randint(1,len(mots))
    mot = mots[i]
    return (mot)


def init():
    '''vérifie l'existence du fichier score, charge les scores et si non existant créé le tout'''
    try:
        with open('pendu_scores','rb') as fichier:
            mon_pickler=pickle.Unpickler(fichier)
            scores = mon_pickler.load()
            print('fichier lu')
            fichier.close
    except:
        with open('pendu_scores','wb') as fichier:
            scores={}
            mon_pickler = pickle.Pickler(fichier)
            mon_pickler.dump(scores)
            print('fichier créé')
            fichier.close
    return scores


def recup_score(joueur):
    try:
        score = scores[joueur]
    except:
        score=0
    return (score)

def ecrit_score(joueur,score):
    scores[joueur]=score
    with open('pendu_scores','wb') as fichier:
            mon_pickler = pickle.Pickler(fichier)
            mon_pickler.dump(scores)
            print('score enregistré')
            fichier.close
    return


def cache_mot(mot):
    mot_cache=[]
    for lettre in mot:
        mot_cache.append('*')
    global let_a_trouv
    let_a_trouv = len(mot)
    return(mot_cache)
   


def cherche_lettre(lettre):
    global let_a_trouv
    i = 0
    for elt in mystere:
        if lettre == elt:
            let_a_trouv -=1
            mot_affiche[i]=lettre
        i+=1
    return()


# scores=init()
# print(scores)
# print(recup_score('Patrice'))
# ecrit_score('Patrice',10)
# print(recup_score('Patrice'))

print(let_a_trouv)
mystere = 'BAGUETTE'
mot_affiche=cache_mot(mystere)
print(mot_affiche)
print(let_a_trouv)
cherche_lettre('T')
print(let_a_trouv)
print(mot_affiche)