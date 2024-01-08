#!/usr/bin/python3
"""Checks subclass"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that inherited\
            (directly or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if the object is an instance of a\
                class that inherited (directly or indirectly) from the\
                specified class; otherwise False.
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
