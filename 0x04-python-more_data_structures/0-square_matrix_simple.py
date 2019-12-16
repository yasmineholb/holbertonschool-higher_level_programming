#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    ss = []
    for i in matrix:
        mm = []
        for j in i:
            mm.append(j**2)
        ss.append(mm)
    return ss
