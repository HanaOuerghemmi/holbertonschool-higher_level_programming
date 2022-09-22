#!/usr/bin/python3
""" devide matrix """


def matrix_divided(matrix, div):
    """fun tion that divides all element of a matrix"""

    if (
        not isinstance(
            matrix,
            list) or matrix == [] or not all(
            isinstance(
                row,
                list) for row in matrix) or not all(
                    (isinstance(
                        case,
                        int) or isinstance(
                            case,
                            float)) for case in [
                                n for row in matrix for n in row])):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
