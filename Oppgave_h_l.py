# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 23:10:30 2023

@author: Mhodne
"""
from lister_for_del_1 import temperaturer


def growth(listname):
    growing = []
    for i in range(len(listname)):
        if listname[i] < 5:
            continue
        else:
            growing.append(listname[i] - 5)
    return growing

print(growth(temperaturer))
