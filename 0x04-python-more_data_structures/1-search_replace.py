#!/usr/bin/python3
def search_replace(my_list, search, replace):
    ss = []
    for j in my_list:
        if j == search:
            ss.append(replace)
        else:
            ss.append(j)
    return(ss)
