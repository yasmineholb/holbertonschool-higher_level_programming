#!/usr/bin/python3
"""
this is an add module
it add integers

"""
def text_indentation(text):
    """
this is the add function
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    t1 = text.replace(".", ".\n\n").replace('?', '?\n\n').replace(':', ':\n\n')
    t = t1.strip(" ")
    print("{:s}".format(t))    
            
