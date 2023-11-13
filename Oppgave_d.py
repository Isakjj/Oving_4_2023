# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 13:59:30 2023

@author: IsakJ
"""

# Define a function which takes a list and one input number as parameters.
# The function checks if each number in the list is equal or bigger than the input number.
# If the number from the list is bigger than the input number, it adds 1 to the resultat-variable.
# At last it prints out the number of elements from the list that are bigger than the input number.
def ant_str(liste, tall):
    resultat = 0
    for i in range(len(liste)):
        try:
            liste_float = float(liste[i])
            if liste_float >= tall:
                resultat += 1
            else: 
                continue
        except ValueError:
            continue
    return resultat


if __name__ == "__main__":
    # Adds a list and an input for a number which the list will be compared to.
    liste = [-5, 2, 6, 13, 9, 22, 28, 19, 24, 12, 5, 1, -3, -8, 2, 8, 15, 18, 21, 26, 21, 31, 15, 4, 1, -2]
    tall = float(input('Hvilket tall vil du sjekke listen opp mot? '))              
    # Print result
    print(ant_str(liste, tall))

