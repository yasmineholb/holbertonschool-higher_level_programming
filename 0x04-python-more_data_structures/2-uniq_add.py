#!/usr/bin/python3
def uniq_add(my_list=[]):
    l = 0
    ss = set(my_list)
    for j in ss:
        l = l + j
    return l
