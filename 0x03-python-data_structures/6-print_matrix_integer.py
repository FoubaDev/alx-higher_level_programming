#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for nested in matrix:
        for value in nested:
            # Compare value to the lats element of nested
            if value != nested[-1]:
                print("{:d}".format(value), end=" ")
            else:
                print("{:d}".format(value), end="")
        print()
