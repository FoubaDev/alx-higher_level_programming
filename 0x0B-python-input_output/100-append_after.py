#!/usr/bin/python3
"""write_file function"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line
    """
    out = ""
    with open(filename, 'r') as f:
        for line in f:
            out += line
            if search_string in line:
                out += new_string

    with open(filename, 'w') as f:
        f.write(out)
