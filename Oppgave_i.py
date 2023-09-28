# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 21:42:50 2023

@author: IsakJ
"""

'''
Henter inn funksjonen fra oppgave d
'''
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
    '''
    Henter inn listen temperaturer fra "lister for del 1"
    '''
    temperaturer = [-5, 2, 6, 13, 9, 22, 28, 19, 24, 12, 5, 1, -3, -8, 2, 8, 15, 18, 21, 26, 21, 31, 15, 4, 1, -2]

    '''
    Bruker funksjonen til å regne ut antall sommerdager, høysommerdager og tropedager.
    Deretter printer vi svarene.
    '''
    sommerdager = ant_str(temperaturer, 21)
    hoysommerdager = ant_str(temperaturer, 26)
    tropedager = ant_str(temperaturer, 31)

    print(f'Det er {sommerdager} dager som kan kategoriseres som sommerdager.')
    print(f'Det er {hoysommerdager} dager som kan kategoriseres som hoysommerdager.')
    print(f'Det er {tropedager} dager som kan kategoriseres som tropedager.')