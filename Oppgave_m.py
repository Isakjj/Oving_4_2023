# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 23:08:33 2023

@author: IsakJ
"""

# Import the function from Oppgave_f and the list "døgn-nedbør from "lister til del 1"
from Oppgave_f import finn_sekvens
from lister_for_del_1 import dogn_nedbor

# Using the function to calculate the longest continous streak of days with rain. 
max_periode_nedbør = finn_sekvens(dogn_nedbor)
print(f'Den lengste perioden med nedbør hvær dag var på {max_periode_nedbør} dager.')