#!/usr/bin/python3
"""write_file module."""


def write_file(filename="", text=""):
    """
    Writes file.
    Args:
        filename (text): name of file
        text (str).
    """
    with open(filename, 'w') as f:
        return f.write(text)
