#!/usr/bin/python3
"""Print square"""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        TypeError: If size is a float and less than 0.
    """
    # Ensure that the size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Ensure that  the size is less than 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # Then print the square
    for _ in range(size):
        print("#" * size)
