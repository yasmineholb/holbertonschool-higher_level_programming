#!/usr/bin/python3
""" pick function """
def find_peak(list_of_integers):
    if len(list_of_integers) >= 2:
        if list_of_integers[0] > list_of_integers[1]:
            return list_of_integers[0]
    for i in range(1, len(list_of_integers) - 1):
        if list_of_integers[i] > list_of_integers[i-1] and  list_of_integers[i] > list_of_integers[i+1]:
            return list_of_integers[i]
        if list_of_integers[i] == list_of_integers[i + 1]:
            return list_of_integers[i]
