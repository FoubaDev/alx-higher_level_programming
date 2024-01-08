#!/usr/bin/python3
"""Write a class MyInt that inherits from int"""


class MyInt(int):
    """Invert int operators == and !=."""

    def __eq__(self, value):
        """
        Changes the inequality (!=) operator to invert its behavior.

        Args:
            other: The object to compare against.

        Returns:
            bool: True if the values are equal, False otherwise.
        """
        return self.real != value

    def __ne__(self, value):
        """change != operator with == behavior."""
        return self.real == value
