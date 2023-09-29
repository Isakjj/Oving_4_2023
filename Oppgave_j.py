# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 23:30:18 2023

@author: Mhodne
"""

from lister_for_del_1 import temperaturer
from Oppgave_e import diff

temp_up_down = diff(temperaturer)

for i in range(len(temp_up_down)):
    if temp_up_down[i] < 0:
        print(i)
        print("The temperature is decreasing.")
    elif temp_up_down[i] > 0:
        print(i)
        print("The temperature is rising.")
    else:
        print(i)
        print("The temperature is unchanged.")