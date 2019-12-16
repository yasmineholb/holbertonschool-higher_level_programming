#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key not in a_dictionary:
        a_dictionary[key] = value
        for i in sorted(a_dictionary):
            print("{}: {}".format(i, a_dictionary[i]))
        
    
