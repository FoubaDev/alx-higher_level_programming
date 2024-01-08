#!/usr/bin/python3
"""Add two integers."""


def add_integer(a, b=98):
    """Adds two integers.

    Args:
        a (int or float): The first argument.
        b (int or float): The second argument. Default value is 98.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b is not an integer or a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or a float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or a float")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return (a + b)
