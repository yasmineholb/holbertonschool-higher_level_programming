#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    ss = matrix[:]
    for i in range(len(ss)):
        for j in range(len(ss[i])):
            ss[i][j] =   matrix[i] * matrix[i]
            return(ss)
