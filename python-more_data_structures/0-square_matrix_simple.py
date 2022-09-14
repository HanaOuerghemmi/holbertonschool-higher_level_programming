#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    Nmatrix = [list(map(lambda x: x * x, row)) for row in matrix]
    return Nmatrix
