#!/usr/bin/python3
"""Module to divide a matrix."""


def matrix_divided(matrix, div):
    """Divides a matrix by a divisor.

    Args:
        matrix(list of lists): The matrix to be divided.
        div(int or float): The divisor.
    Raises:
        TypeError: If the matrix elements are not integers or floats.
        TypeError: If the rows of the matrix have different sizes.
        TypeError: If the divisor is not an integer or float.
        ZeroDivisionError: If the divisor is 0.
    Returns:
        A list of lists: The new matrix with elements divided by the divisor.
    """

    if not all(isinstance(row, list) for row in matrix) or \
            not all(all(isinstance(e, (int, float)) for e in row)
                    for row in matrix):
        raise\
                TypeError("matrix must be a matrix\
                (list of lists) of integers/floats")

    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(e / div, 2) for e in row] for row in matrix]
    return (new_matrix)
