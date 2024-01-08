#!/usr/bin/python3
"""
Define a function that returns a list off
available attributes
"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object"""
    return (dir(obj))
