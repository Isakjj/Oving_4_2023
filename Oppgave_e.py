# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 00:06:44 2023

@author: Mhodne
"""

def diff(listname):
    #Makes a new list outside the loop
    newlist = []
    #The loop runs for as many elements in the list.
    for i in range(1,len(listname)):
            #Makes a new variabel thats the difference between one element and the element below in the list.
            diff = int(listname[i]) - int(listname[i-1])
            #Puts the new element into the new list.
            newlist.append(diff)
    #Return the new list.
    return newlist

if __name__ == "__main__":
    listname = [1, 4, 6, 7, 9, 13, 14, 22, 24, 25]
#Makes a new variable and sets gives it the value og the new list.      
    difflist = diff(listname)
    print(difflist)
       