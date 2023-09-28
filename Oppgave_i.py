# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 21:42:50 2023

@author: IsakJ
"""
# Import function from Oppgave d and the list "temperaturer" from "lister til del 1"
from Oppgave_d import ant_str
from lister_for_del_1 import temperaturer

# Use the function ant_str to calculate the ammount of days with a max temp
# over 20, 25 and 30 degrees, and then print the answers.
sommerdager = ant_str(temperaturer, 21)
hoysommerdager = ant_str(temperaturer, 26)
tropedager = ant_str(temperaturer, 31)

print(f'Det er {sommerdager} dager som kan kategoriseres som sommerdager.')
print(f'Det er {hoysommerdager} dager som kan kategoriseres som hoysommerdager.')
print(f'Det er {tropedager} dager som kan kategoriseres som tropedager.')