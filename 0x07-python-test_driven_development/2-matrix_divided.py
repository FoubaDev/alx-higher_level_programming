#!/usr/bin/python3

"""Divide all element matrix"""


def matrix_divided(matrix, div):
    """
    Divides a matrix.

    Args:
        matrix (int element) : given matrix.
        div (int) : a divider
    Returns:
        matrix (int element): new matrix
    Raises:
        TypeError: if element are not int or float.
        TypeError: if different row size.
        TypeError: if divider in not  int or float.
        ZeroDivisionError: if divider is 0.
    """

    # Check if matrix is a list of lists of integers or floats
    if not all(isinstance(row, list) for row in matrix)\
            or not all(all(isinstance(e, (int, float))
            for e in row) for row in matrix):
        raise TypeError("matrix must be a matrix(list of lists)" +
                "of integers/floats")
    # Ensure that the rows have the same size
    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Ensure that div in a int or float
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # For element (e) of matrix, divide it by div rounded to 2 decimal places
    new_matrix = [[round(e / div, 2) for e in row] for row in matrix]

    return new_matrix
