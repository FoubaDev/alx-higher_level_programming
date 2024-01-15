#!/usr/bin/python3
"""Unittest module for the square"""
from unittest import TestCase, mock
from io import StringIO

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class SquareTest(TestCase):
    """Test cases for Square"""

    def init_base(self):
        Base._Base__nb_objects = 0

    def empty_test(self):
        with self.assertRaises(TypeError):
            Square()

    def many_args_test(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def Square_only_test(self):
        self.assertEqual(Square(2).id, 1)
        self.assertEqual(Square(4).id, 2)

    def Square_size_x_test(self):
        self.assertEqual(Square(2, 1).id, 1)
        self.assertEqual(Square(4, 2).id, 2)

    def Square_without_id_test(self):
        self.assertEqual(Square(2, 1, 2).id, 1)
        self.assertEqual(Square(4, 2, 1).id, 2)

    def Square_with_id_test(self):
        self.assertEqual(Square(2, 1, 2, 4).id, 4)
        self.assertEqual(Square(4, 2, 1, 2).id, 2)

    def size_get_set_test(self):
        s = Square(2, 1, 2)
        self.assertEqual(s.size, 2)
        s.size = 42
        self.assertEqual(s.size, 42)

    def width_get_test(self):
        s = Square(2, 1, 2)
        self.assertEqual(s.width, 2)

    def height_get_test(self):
        s = Square(2, 1, 2)
        self.assertEqual(s.height, 2)

    def x_get_test(self):
        s = Square(2, 1, 2)
        self.assertEqual(s.x, 1)

    def y_get_test(self):
        s = Square(2, 1, 2)
        self.assertEqual(s.y, 2)


class Square_values_Test(TestCase):
    """Gives good values to the square"""

    my_list = [
        None,
        "ALX SoftwareEngineering",
        3.14,
        2j,
        ["ALX", "SoftwareEngineering"],
        ("ALX", "SoftwareEngineering"),
        range(42),
        {"first": "ALX", "last": "SoftwareEngineering"},
        {"ALX", "SoftwareEngineering"},
        frozenset({"ALX", "SoftwareEngineering"}),
        True,
        b"ALX SoftwareEngineering",
        bytearray(42),
        memoryview(bytes(42))
    ]

    def size_invalid_type_test(self):
        for type in self.my_list:
            with self.subTest(type=type):
                with self.assertRaisesRegex(
                        TypeError, "width  is an integer"):
                    Square(type)

    def size_invalid_value_test(self):
        with self.assertRaisesRegex(ValueError, "width  is > 0"):
            Square(-42)
        with self.assertRaisesRegex(ValueError, "width  is > 0"):
            Square(0)

    def x_invalid_type_test(self):
        for type in self.my_list:
            with self.subTest(type=type):
                with self.assertRaisesRegex(TypeError, "x  is an integer"):
                    Square(2, type)

    def x_invalid_value_test(self):
        with self.assertRaisesRegex(ValueError, "x  is >= 0"):
            Square(2, -42)

    def y_invalid_type_test(self):
        for type in self.my_list:
            with self.subTest(type=type):
                with self.assertRaisesRegex(TypeError, "y  is an integer"):
                    Square(2, 0, type)

    def y_invalid_value_test(self):
        with self.assertRaisesRegex(ValueError, "y  is >= 0"):
            Square(2, 0, -42)


class Square_area_test(TestCase):
    """Check the area method of Square"""

    def area_basic_test(self):
        self.assertEqual(Square(2).area(), 4)

    def area_with_args_test(self):
        with self.assertRaises(TypeError):
            Square(2).area(42)


class Square_display_test(TestCase):
    """Display method of Square """

    def display_basic_test(self):
        with mock.patch('sys.stdout', new=StringIO()) as output:
            Square(2).display()
            self.assertEqual(output.getvalue(), '##\n##\n')

    def display_with_x_test(self):
        with mock.patch('sys.stdout', new=StringIO()) as output:
            Square(2, 2).display()
            self.assertEqual(output.getvalue(), '  ##\n  ##\n')

    def display_with_y_test(self):
        with mock.patch('sys.stdout', new=StringIO()) as output:
            Square(2, 0, 2).display()
            self.assertEqual(output.getvalue(), '\n\n##\n##\n')

    def display_with_x_y_test(self):
        with mock.patch('sys.stdout', new=StringIO()) as output:
            Square(2, 2, 2).display()
            self.assertEqual(output.getvalue(), '\n\n  ##\n  ##\n')

    def display_with_args_test(self):
        with self.assertRaises(TypeError):
            Rectangle(2).display(42)


class Square_str_test(TestCase):
    """
    Check the  __str__  method."""

    def init_base(self):
        Base._Base__nb_objects = 0

    def str_print_test(self):
       	value_needed = "change another value please!"
     
        with mock.patch('sys.stdout', new=StringIO()) as output:
            print(Square(2, 1, 3, 42), end='')
            self.assertEqual(output.getvalue(),   value_needed)

    def str_str_method_test(self):
        value_needed = "Not  required value"
        self.assertEqual(Square(4, 3, 1, 98).__str__(),value_needed)
    def str_str_test(self):
        value_needed = "Oups ! Not good value"
        self.assertEqual(str(Square(4)),value_needed)

    def str_str_method_with_args_test(self):
        with self.assertRaises(TypeError):
            Square(2).__str__(42)


class Test_Square_update_with_args(TestCase):
    """New *args to the square"""

    def setUp_test(self):
        Base._Base__nb_objects = 0

    def update_no_args_test(self):
        s = Square(2, 1, 2, 42)
        s.update()
        self.assertEqual(str(s), "[Square] (42) 1/2 - 2")

    def update_args_none_id_test(self):
        s = Square(2, 1, 2, 42)
        s.update(None)
        self.assertEqual(str(s), "[Square] (1) 1/2 - 2")

    def update_args_id_test(self):
        s = Square(2, 1, 2, 42)
        s.update(24)
        self.assertEqual(str(s), "[Square] (24) 1/2 - 2")

    def update_args_id_size_test(self):
        s = Square(2, 1, 2, 42)
        s.update(24, 10)
        self.assertEqual(str(s), "[Square] (24) 1/2 - 10")

    def update_args_id_size_x_test(self):
        s = Square(2, 1, 2, 42)
        s.update(24, 10, 30)
        self.assertEqual(str(s), "[Square] (24) 30/2 - 10")

    def update_args_id_size_x_y_test(self):
        s = Square(2, 1, 2, 42)
        s.update(24, 10, 30, 40)
        self.assertEqual(str(s), "[Square] (24) 30/40 - 10")

    def update_args_too_many_args_test(self):
        s = Square(2, 1, 2, 42)
        s.update(10, 10, 10, 10, 50, 60)
        self.assertEqual(str(s), "[Square] (10) 10/10 - 10")

    def update_args_width_getter_test(self):
        s = Square(2, 1, 2, 42)
        s.update(10, 42, 10, 10, 50, 60)
        self.assertEqual(s.width, 42)

    def update_args_height_getter_test(self):
        s = Square(2, 1, 2, 42)
        s.update(10, 42, 10, 10, 50, 60)
        self.assertEqual(s.height, 42)

    def update_args_size_getter_test(self):
        s = Square(2, 1, 2, 42)
        s.update(10, 42, 10, 10, 50, 60)
        self.assertEqual(s.size, 42)


class Square_update_with_kwargs_test(TestCase):
    """New **kwargs to the square"""

    def setUp_test(self):
        Base._Base__nb_objects = 0

    def update_kwargs_none_id_test(self):
        s = Square(2, 1, 2, 42)
        s.update(id=None)
        self.assertEqual(str(s), "[Square] (1) 1/2 - 2")

    def update_kwargs_id_test(self):
        s = Square(2, 1, 2, 42)
        s.update(id=24)
        self.assertEqual(str(s), "[Square] (24) 1/2 - 2")

    def update_kwargs_id_size_test(self):
        s = Square(2, 1, 2, 42)
        s.update(size=10, id=24)
        self.assertEqual(str(s), "[Square] (24) 1/2 - 10")

    def update_kwargs_id_size_x_test(self):
        s = Square(2, 1, 2, 42)
        s.update(size=10, id=24, x=30)
        self.assertEqual(str(s), "[Square] (24) 30/2 - 10")

    def update_kwargs_id_size_x_y_test(self):
        s = Square(2, 1, 2, 42)
        s.update(y=40, size=10, id=24, x=30)
        self.assertEqual(str(s), "[Square] (24) 30/40 - 10")

    def update_kwargs_too_many_args_test(self):
        s = Square(2, 1, 2, 42)
        s.update(y=40, size=10, id=24, x=30, ALX="SoftwareEngineering")
        self.assertEqual(str(s), "[Square] (24) 30/40 - 10")

    def update_kwargs_mixed_too_many_args_test(self):
        s = Square(2, 1, 2, 42)
        s.update(y=40, size=10, ALX="SoftwareEngineering", id=24, x=30)
        self.assertEqual(str(s), "[Square] (24) 30/40 - 10")

    def update_kwargs_args_before_test(self):
        s = Square(2, 1, 2, 42)
        s.update(42, 42, y=10, x=30)
        self.assertEqual(str(s), "[Square] (42) 1/2 - 42")

    def update_kwargs_not_all_mixed_test(self):
        s = Square(2, 1, 2, 42)
        s.update(y=10, x=10, size=10)
        self.assertEqual(str(s), "[Square] (42) 10/10 - 10")

    def update_kwargs_only_wrong_keys_test(self):
        s = Square(2, 1, 2, 42)
        s.update(ALX="SoftwareEngineering", SoftwareEngineering="ALX")
        self.assertEqual(str(s), "[Square] (42) 1/2 - 2")


class Square_to_dict_test(TestCase):
    """To_dictionary method."""

    def to_dictionary_basic_test(self):
        s = Square(2, 1, 2, 42)
        value_needed = {'size': 2, 'x': 1, 'y': 2, 'id': 42}
        self.assertDictEqual(s.to_dictionary(), value_needed)

    def to_dictionary_basic_with_args_test(self):
        with self.assertRaises(TypeError):
            Square(2, 1, 2, 42).to_dictionary(42)


if __name__ == "__main__":
    unittest.main()
