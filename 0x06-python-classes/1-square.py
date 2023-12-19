#!/usr/bin/python3

"""Define a class Square"""


class Square:

    """
    A square that has private attribute size
    """
    def __init__(self, size):
        """
        Create an instance  of Square

        Args:
            size(int): size to define a area of square

        """
        self.__size = size
