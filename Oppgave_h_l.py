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
        growing.append(listname[i] - 5)
    return sum(growing)

if __name__ == '__main__':
    print(growth(temperaturer))
