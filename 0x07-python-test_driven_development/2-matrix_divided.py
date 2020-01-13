#!/usr/bin/python3

"""Function that divides all element of a matrix.
    arg:
    matrix:(int/float): matrix of list
    div: (int/float): divisor number
"""


def matrix_divided(matrix, div):
    """
        Functions that divides all elements of a matrix.
    """
    length = 0
    new_matrix = []
    err = "matrix must be a matrix (list of lists) of integer o float"

    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    length = len(matrix[0])

    for i in matrix:
        if not isinstance(i, list):
            raise TypeError(err)
        if len(i) != length:
            raise TypeError("Each row of the matrix must have the same size")
        a = []
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError(err)

            a.append(round(j / div, 2))
        new_matrix.append(a)
    return new_matrix
