#!/usr/bin/python3
"""Print my name"""


def say_my_name(first_name, last_name=""):
    """
    Says my name.
    Args:
        first_name(str): the first_name
        last_name(str): the last_name
    Raises:
        TypeError: if firstname is not string
        TypeError: if last_name is not string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
