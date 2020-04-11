# -*-coding:utf-8 -*
import os



# ma_liste = list() #on crée une liste vide
# ma_liste =[1,2,3,4,5]
# print(ma_liste)

# ma_liste=[1,3.5,"trois et demi"]
# print(ma_liste)

# ma_liste = ['c','f','m']
# print(ma_liste[0])
# print(ma_liste[2])
# ma_liste[1]='Z'
# print(ma_liste)

# # Parcours de liste
# ma_liste=['a','b','c','d','e','f','g','h']
# i=0
# while i < len(ma_liste):
#     print(ma_liste[i])
#     i +=1

# for individu in ma_liste:
#     print(individu) 

# ma_liste=['a','b','c','d','e','f','g','h']
# for elt in enumerate(ma_liste):
    # print(elt)
# 
# for i, elt in enumerate(ma_liste):
    # print("À l'indice {} se trouve {}".format(i, elt))


# ma_chaine = "Bonjour à tous !"
# # print(ma_chaine.split(" "))
# ma_liste = ma_chaine.split(" ")
# # print(ma_liste)
# ma_chaine= " ".join(ma_liste)
#print(ma_chaine)


# # à partir de 3.999999999998 afficher 3,999
# def afficher_flottant(nombre):
#     partie_entiere, partie_flottante = str(nombre).split('.')
#     return ",".join([partie_entiere, partie_flottante[:3]])
#     # 
    
# print(afficher_flottant(3.99999999999998))


# def afficher(*parametres, sep='i', fin='/n'):
#     """Fonction chargée de reproduire le comportement de print.
    
#     Elle doit finir par faire appel à print pour afficher le résultat.
#     Mais les paramètres devront déja avoir été formatés.
#     On doit passer à print une unique chaine, en lui spécifiant de ne rien mettre à la fin :

#     print(chaine, end=' ')"""

#     parametres = list(parametres)

#     for i, parametre in enumerate(parametres):
#         parametres[i] = str(parametre)

#     chaine = sep.join(parametres)
#     chaine += fin
#     print(chaine, end="")

# afficher("Bonjour" "tout" "le" "monde")

# # simplification de listes
# liste_depart=[1,2,3,4,5,6,7,8,10]
# liste_carre=[nb * nb for nb in liste_depart]
# liste_pair=[nb for nb in liste_depart if nb %2 == 0]
# print (liste_carre)
# print(liste_pair)

# # inventaire à trier
# inventaire =[
#     ("pommes",22),
#     ("melons",4),
#     ("poires", 18),
#     ("fraises",76),
#     ("Prunes",51)
# ]
# inventaire = [(qte, fruit) for fruit,qte in inventaire] # on inverse la qté et les fruits
# # inventaire =[(fruit,qte) for qte,fruit in sorted(inventaire,reverse=True)]

# inventaire.sort(reverse=True)
# inventaire =[(fruit,qte) for qte,fruit in inventaire]
# print(inventaire)


