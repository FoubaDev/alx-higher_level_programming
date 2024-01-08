#!/usr/bin/python3
"""Test max integer function"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class MaxIntegerTest(unittest.TestCase):
    """Test using unitest for max_integer"""
    
    def max_at_begginning_test(self):
        """Test a max at begining"""
        max_at_beginning = [6, 5, 4, 2]
        self.assertEqual(max_integer(max_at_beginning), 6)
    
    def empty_list_test(self):
        """Test when a list is empty."""
        empty = []
        self.assertEqual(max_integer(empty), None)
    
    def one_element_list_test(self):
        """Test when just one element in a list."""
        one_element = [10]
        self.assertEqual(max_integer(one_element), 10)

    def floats_test(self):
        """Test a list of floats."""
        floats = [5, -13.33, 4.3, 9.0, 5.6]
        self.assertEqual(max_integer(floats), 9.0)
    
    def unordered_list_test(self):
        """Test list with max in middle"""
        unordered = [3, 6, 7, 5]
        self.assertEqual(max_integer(unordered), 7)

    def ints_and_floats_test(self):
        """Test float and int elements"""
        ints_and_floats = [23.5, 30.666, -4, 5, 10]
        self.assertEqual(max_integer(ints_and_floats), 30.666)
        
    def ordered_list_test(self):
        """Test a list with ordered int element"""
        ordered = [6, 7, 8, 9]
        self.assertEqual(max_integer(ordered), 9)

    def string_test(self):
        """Test a string."""
        string = "foubadev"
        self.assertEqual(max_integer(string), 'v')

    def list_of_strings_test(self):
        """Test a list with strings elements."""
        strings = ["Datascientist", "is", "my", "passion"]
        self.assertEqual(max_integer(strings), "passion")

    def empty_string_test(self):
        """Test when a list is empty."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
