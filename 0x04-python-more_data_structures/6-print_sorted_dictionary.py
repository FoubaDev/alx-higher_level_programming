#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ordered_key = sorted(a_dictionary.keys())
    for key in ordered_key:
        value = a_dictionary[key]
        print("{}: {}".format(key, value))
