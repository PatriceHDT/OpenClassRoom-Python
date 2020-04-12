# -*-coding:utf-8 -*
import os

# mon_dictionnaire = dict()
# mon_dictionnaire ["pseudo"]="prolixe"
# mon_dictionnaire ["mot de passe"]="*"
# print(mon_dictionnaire)
# mon_dictionnaire = {"mot de passe":'*', 'pseudo':'6pril'}
# print(mon_dictionnaire)


fruits = {"pommes":21, "melons":3, "poires":31}
for cle in fruits.keys():
    print(cle)


fruits = {"pommes":21, "melons":3, "poires":31}
for cle,valeur in fruits.items():
    print("la clé {} contient la valeur {}.".format(cle,valeur))



