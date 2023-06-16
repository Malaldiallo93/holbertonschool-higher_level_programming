#!/usr/bin/python3
"""Module that divides all elements of a matrix and return a new matrix
    Args:
        matrix (list of lists): two-dimensional data structure
        div (int, floats): divider
"""


def matrix_divided(matrix, div):
    """Function that divides all elements of a
    matrix by div and return a new matrix.
    """

    """Verify if matrix is a list"""
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)\
of integers/floats")

    for row in matrix:
        """Verify if each row is a list"""
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
        for element in row:
            """Verify types of elements in the matrix"""
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")

    """Verify if row sizes in the matrix is equal"""
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

    """Verify division by 0"""
    if div == 0:
        raise ZeroDivisionError("division by zero")

    """Verify type of div"""
    if not isinstance(div, (int, float)) or div is None:
        raise TypeError("div must be a number")

    new_matrix = [[round(element/div, 2) for element in row] for row in matrix]
    return new_matrix
