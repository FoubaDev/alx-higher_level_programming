#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for subset in matrix:
        output = " ".join(str(element) for element in subset)
        print("{}".format(output))
