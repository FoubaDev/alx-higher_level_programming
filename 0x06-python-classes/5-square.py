#!/usr/bin/python3

"""Define a class Square"""


class Square:

    """
    A square that has private attribute size
    """
    def __init__(self, size=0):
        """
        Create an instance  of Square

        Args:
            size(int): size to define a area of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """
        Define a property to retrieve size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Define a setter property to set size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        A function that calculate the aeza of a square
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints in stdout the square with the character #:
        if size is equal to 0, print an empty line
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
