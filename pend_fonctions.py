
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
            fichier.close
    except:
        with open('pendu_scores','wb') as fichier:
            scores={}
            mon_pickler = pickle.Pickler(fichier)
            mon_pickler.dump(scores)
            fichier.close
    return scores


def recup_score(joueur):
    scores=init() 
    try:
        score = scores[joueur]
    except:
        score=0
    return (score)

def ecrit_score(joueur,score):
    scores=init()
    scores[joueur]=score
    with open('pendu_scores','wb') as fichier:
            mon_pickler = pickle.Pickler(fichier)
            mon_pickler.dump(scores)
            fichier.close
    return


def cache_mot(mot):
    mot_cache=[]
    for lettre in mot:
        mot_cache.append('*')
    let_a_trouv = len(mot)
    return(mot_cache,let_a_trouv)
   
def recup_lettre():
    lettre = input ("Saisissez une lettre : ")
    lettre = lettre.upper()
    if len(lettre) !=1:
        return recup_lettre()
    return(lettre)


def cherche_lettre(mystere,lettre,mot_affiche,let_a_trouv,essai):
    i = 0
    trouve=0
    for elt in mystere:
        if lettre == elt:
            let_a_trouv -=1
            mot_affiche[i]=lettre
            trouve=1
        i +=1
    if trouve == 0:
        essai +=1
    return(mot_affiche,let_a_trouv,essai)

