#!/usr/bin/python3
"""Write a class LockedClass"""


class LockedClass:
    """
    Prevents the user from dynamically creating new instance.
    Attributes:
            firstname (str): attibute that allows to init
    """

    __slots__ = ["first_name"]
