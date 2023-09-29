# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 14:27:58 2023

@author: IsakJ
"""
# Define a function that has a list as parameter, which can find the longest sequence in a list.
def finn_sekvens(liste,tall=None):
    resultat = 1
    ferdig_resultat = 0
    for i in range(len(liste)-1):
        if liste[i] == liste[i+1] and (liste[i]==tall or tall==None):
            resultat += 1
        else:
            if resultat >= ferdig_resultat:
                ferdig_resultat = resultat
                resultat = 1
            else:
                resultat = 1
    if resultat >= ferdig_resultat:
        ferdig_resultat = resultat 
    return ferdig_resultat


if __name__ == "__main__":
    liste = [1,1,2,2,2,2,2,2,3,3,3,3,-3,-3,-3,-3,-3,-3,-3,-3,-3]
    print(finn_sekvens(liste))


