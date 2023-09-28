# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 13:59:30 2023

@author: IsakJ
"""
"""
Definerer en funksjon som tar inn en liste og et enkelt tall som parametere.
Funksjonen sjekker om hvert av tallene i lista er lik eller større enn input tallet.
Hvis listetallet er større eller lik inputtallet, legger den til 1 i resultatvariabelen, og går videre til neste del av lista 
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

if __name__ == "__main__":
    #Legger inn en liste og en input for tallet som en sjekker listen opp mot
    liste = [-5, 2, 6, 13, 9, 22, 28, 19, 24, 12, 5, 1, -3, -8, 2, 8, 15, 18, 21, 26, 21, 31, 15, 4, 1, -2]
    tall = float(input('Hvilket tall vil du sjekke listen opp mot? '))              
    #printer resultatet
    print(ant_str(liste, tall))

