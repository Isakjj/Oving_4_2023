# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 23:08:33 2023

@author: IsakJ
"""

'''
Henter funksjonen fra oppgave f
'''
#Skal vær her


'''
Henter lista "døgn-nedbør" fra lister til del 1
'''
dogn_nedbor = [2, 5, 0, 0, 0, 3, 6, 4, 0, 0, 5, 0, 12, 12, 12, 12, 7, 19]


'''
Bruker her funksjonen til å regne ut og printer deretter svaret.
'''
max_periode_nedbør = finn_sekvens(dogn_nedbor)

print(f'Den lengste perioden med nedbør hvær dag var på {max_periode_nedbør} dager.')