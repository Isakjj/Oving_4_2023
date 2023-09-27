# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 15:19:19 2023

@author: Mhodne
"""

def trend(x, y):
    #Finding the average values for the x and y lists.
    x_average = sum(x) / len(x)
    y_average = sum(y) / len(y)

    #Calculates the numerator for the equation. 
    #The line calculates the deviation from the average for each element in x and y.
    #Then multiplies the x and y deviations and saves them in a list.
    #Then adds all the elements from this new list together and sets the numerator equal to this sum.
    #zip iterator tuples
    numerator = sum([(xi - x_average) * (yi - y_average) for xi, yi in zip(x, y)])
    #This does the same just for the denominator and only with xi and x.
    denominator = sum([(xi - x_average) ** 2 for xi in x])

    #Calculates the slope and intersect values for the line.
    a = round(numerator / denominator, 4) 
    b = round(y_average - a * x_average, 4)
     
    return a, b


if __name__ == "__main__":
    #x-coordinates
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #y-coordinates
    list2 = [1, 4, 6, 7, 9, 13, 14, 22, 24, 25]                   
    a, b = trend(list1, list2)
    print(f"The slope number is {a}")
    print(f"The intersect value is {b}")



