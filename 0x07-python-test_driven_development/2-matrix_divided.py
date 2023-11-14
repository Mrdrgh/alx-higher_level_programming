#!/usr/bin/python3
""" divide a matrix"""


def matrix_divided(matrix, div):
    res =[[]]
    len = len(matrix[i])
    ii = 0
    jj = 0
    for i in matrix:
        if len(i) is not len:
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            res[ii][jj] = j / div
            jj += 1
        ii += 1
    return (res)