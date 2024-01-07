#!/usr/bin/python3
""" Add two integers"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int of float) : first argument
        b (int of float) : second argument.

    Returns:
        int : Addtion of a and b.
    Raises:
        TypeError: if a or b is not integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
