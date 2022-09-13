#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return None
    for row in matrix:
        for i in row:
            if row.index(i) != 0:
                print(" ", end="")
            print("{:d}".format(i), end="")
        print()
