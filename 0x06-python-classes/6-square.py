#!/usr/bin/python3

"""Define a class Square"""


class Square:

    """
    A square that has private attribute size
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Create an instance  of Square

        Args:
            size(int): size to define a area of square
            position(int): square poistion (x,y)
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Define a property to retrieve size
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Define a setter property to set size
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(num, int) for num in value) or \
                not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
