#!/usr/bin/python3
"""append_write module."""


def append_write(filename="", text=""):
    """
    Appends a string.
    Args:
        filename(str): name of file
        text (str): text
    """
    with open(filename, 'a') as f:
        return f.write(text)
