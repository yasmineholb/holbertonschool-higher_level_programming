#!/usr/bin/python3
"""
this is text module
it does identation in text

"""


def text_indentation(text):
    """
this is the text function
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    t1 = text.replace(".", ".\n\n").replace('?', '?\n\n').replace(':', ':\n\n')
    t = t1.strip(" ")
    print("{:s}".format(t))    
            
