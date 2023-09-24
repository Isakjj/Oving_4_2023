# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 00:06:44 2023

@author: Mhodne
"""

#Skriv en funksjon som tar inn ei liste med tall. For hvert tall i lista unntatt det siste skal
#funksjonen regne ut differansen mellom neste tall i lista og dette tallet. Differansene skal
#legges inn i ei ny liste.


listname = [-8, -5, -4, -2, 1, 3, 7, 9, 11, 17]

def diff(listname):
    #Lager en ny liste utenfor for loopen.
    newlist = []
    i = 0
    #For loopen kjører for så mange elementer som er i listen 
    for element in range(1, len(listname)):
            #Lager en ny variabel som er differansen mellom et element og elementet under.
            diff = int(listname[i+1]) - int(listname[i])
            #Legger den nye variabelen inn i den nye listen.
            newlist.append(diff)
            #Legger til en slik at regnestykket flytter seg et element opp listen.
            i += 1
    #Returnerer den nye listen
    return newlist


#Lager en variabel som blir satt lik den nye listen.       
difflist = diff(listname)
print(difflist)
       