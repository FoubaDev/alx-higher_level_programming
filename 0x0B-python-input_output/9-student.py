#!/usr/bin/python3
"""Student classr."""


class Student():
    """Defines a Student."""

    def __init__(self, first_name, last_name, age):
        """Inits attributes for the Student object.

        Args:
            first_name (str): first name of the student.
            last_name (str): last name of the student.
            age (int): age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Loads a  Student instance."""
        return self.__dict__
