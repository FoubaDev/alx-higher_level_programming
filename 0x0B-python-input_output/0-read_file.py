#!/usr/bin/python3
"""Read file"""


def read_file(filename=""):
    """
    Read file from input
    Args:
        filename (str): the given file.
    """
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
