# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 13:59:30 2023

@author: IsakJ
"""

def ant_str(liste, tall):
    resultat = 0
    for i in range(len(liste)):
        liste_float = float(liste[i])
        if liste_float >= tall:
                resultat += 1
        else: 
            continue
    return resultat
    

liste = list(input('Hvilken liste vil du sjekke? '))
tall = float(input('Hvilket tall vil du sjekke listen opp mot? '))              
ant_str(liste, tall)
