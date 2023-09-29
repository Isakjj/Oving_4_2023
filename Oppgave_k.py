# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 22:55:33 2023

@author: Mhodne
"""

from lister_for_del_1 import temperaturer
from lister_for_del_1 import temperaturer_tidspunkter
from Oppgave_g import trend

slope,intersect = trend(temperaturer_tidspunkter, temperaturer)

if slope > 0:
    print("The trend is rising.")
elif slope < 0:
    print("The trend is decreasing.")
else:
    print("No trend.")