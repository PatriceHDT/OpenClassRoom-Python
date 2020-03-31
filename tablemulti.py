# -*-coding:utf-8 -*
import os

def Multiplication (nb, max):
    i = 0
    while i < max: # On se limite à la table des 10
        print (i +1, "*", nb, "=", (i+1) * nb )
        i += 1 # On incrémente i

# test de la fonction multiplication

if __name__ == "__main__" :
    Multiplication (7,12)
    os.system("pause")



