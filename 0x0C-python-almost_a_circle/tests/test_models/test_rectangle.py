#!/usr/bin/python3
"""This is the rectangle.py unittest module."""
from unittest import TestCase, mock
from io import StringIO

from models.base import Base
from models.rectangle import Rectangle


class Rectangle_basics_test(TestCase):
    """Rectangle initialization."""

    def init_base(self):
        Base._Base__nb_objects = 0

    def empty_test(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def one_arg_missing_test(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def too_many_args_test(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def Rectangle_only_required_test(self):
        self.assertEqual(Rectangle(2, 4).id, 1)
        self.assertEqual(Rectangle(4, 2).id, 2)

    def Rectangle_width_height_x_test(self):
        self.assertEqual(Rectangle(2, 4, 1).id, 1)
        self.assertEqual(Rectangle(4, 2, 2).id, 2)

    def Rectangle_no_id_test(self):
        self.assertEqual(Rectangle(2, 4, 1, 2).id, 1)
        self.assertEqual(Rectangle(4, 2, 2, 1).id, 2)

    def Rectangle_with_id_test(self):
        self.assertEqual(Rectangle(2, 4, 1, 2, 4).id, 4)
        self.assertEqual(Rectangle(4, 2, 2, 1, 2).id, 2)

    def width_get_set_test(self):
        r = Rectangle(2, 4, 1, 2)
        with self.assertRaises(AttributeError):
            r.__width
        self.assertEqual(r.width, 2)
        r.width = 42
        self.assertEqual(r.width, 42)

    def height_get_set_test(self):
        r = Rectangle(2, 4, 1, 2)
        with self.assertRaises(AttributeError):
            r.__height
        self.assertEqual(r.height, 4)
        r.height = 42
        self.assertEqual(r.height, 42)

    def x_get_set_test(self):
        r = Rectangle(2, 4, 1, 2)
        with self.assertRaises(AttributeError):
            r.__x
        self.assertEqual(r.x, 1)
        r.x = 42
        self.assertEqual(r.x, 42)

    def y_get_set_test(self):
        r = Rectangle(2, 4, 1, 2)
        with self.assertRaises(AttributeError):
            r.__y
        self.assertEqual(r.y, 2)
        r.y = 42
        self.assertEqual(r.y, 42)


class Rectangle_values_test(TestCase):
    """Rectangle input, getter and setter"""

    my_types = [
        None,
        "ALX Software",
        3.14,
        2j,
        ["ALX", "Software"],
        ("ALX", "Software"),
        range(42),
        {"first": "ALX", "last": "Software"},
        {"ALX", "Software"},
        frozenset({"ALX", "Software"}),
        True,
        b"ALX Software",
        bytearray(42),
        memoryview(bytes(42))
    ]

    def width_invalid_type_test(self):
        for type in self.my_types:
            with self.subTest(type=type):
                with self.assertRaisesRegex(
                        TypeError, "width is an integer"):
                    Rectangle(type, 4)

    def width_invalid_value_test(self):
        with self.assertRaisesRegex(ValueError, "width is > 0"):
            Rectangle(-42, 4)
        with self.assertRaisesRegex(ValueError, "width is > 0"):
            Rectangle(0, 4)

    def height_invalid_type_test(self):
        for type in self.my_types:
            with self.subTest(type=type):
                with self.assertRaisesRegex(
                        TypeError, "height is an integer"):
                    Rectangle(2, type)

    def height_invalid_value_test(self):
        with self.assertRaisesRegex(ValueError, "height is > 0"):
            Rectangle(2, -42)
        with self.assertRaisesRegex(ValueError, "height is > 0"):
            Rectangle(2, 0)

    def x_invalid_type_test(self):
        for type in self.my_types:
            with self.subTest(type=type):
                with self.assertRaisesRegex(TypeError, "x is an integer"):
                    Rectangle(2, 4, type)

    def x_invalid_value_test(self):
        with self.assertRaisesRegex(ValueError, "x is >= 0"):
            Rectangle(2, 4, -42)

    def y_invalid_type_test(self):
        for type in self.my_types:
            with self.subTest(type=type):
                with self.assertRaisesRegex(TypeError, "y is an integer"):
                    Rectangle(2, 4, 0, type)

    def y_invalid_value_test(self):
        with self.assertRaisesRegex(ValueError, "y is >= 0"):
            Rectangle(2, 4, 0, -42)


class Rectangle_area_test(TestCase):
    """Rectangle's area method."""

    def area_basic_test(self):
        self.assertEqual(Rectangle(2, 4).area(), 8)

    def area_with_args_test(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 4).area(42)


class Rectangle_display_test(TestCase):
    """Rectangle's display method."""

    def display_basic_test(self):
        with mock.patch('sys.stdout', new=StringIO()) as output:
            Rectangle(2, 4).display()
            self.assertEqual(output.getvalue(), '##\n##\n##\n##\n')

    def display_with_x_test(self):
        with mock.patch('sys.stdout', new=StringIO()) as output:
            Rectangle(2, 4, 2).display()
            self.assertEqual(output.getvalue(), '  ##\n  ##\n  ##\n  ##\n')

    def display_with_y_test(self):
        with mock.patch('sys.stdout', new=StringIO()) as output:
            Rectangle(2, 4, 0, 2).display()
            self.assertEqual(output.getvalue(), '\n\n##\n##\n##\n##\n')

    def display_with_x_y_test(self):
        with mock.patch('sys.stdout', new=StringIO()) as output:
            Rectangle(2, 4, 2, 2).display()
            self.assertEqual(output.getvalue(), '\n\n  ##\n  ##\n  ##\n  ##\n')

    def display_with_args_test(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 4).display(42)


class Rectangle_str_test(TestCase):
    """Rectangle's __str__ method."""

    def init_base(self):
        Base._Base__nb_objects = 0

    def str_print_test(self):
        value_needed = "change another value please!"
        with mock.patch('sys.stdout', new=StringIO()) as output:
            print(Rectangle(2, 4, 1, 3, 42), end='')
            self.assertEqual(output.getvalue(), value_needed)

    def str_str_method_test(self):
        value_needed = "[Rectangle] (98) 3/1 - 4/2"
        self.assertEqual(Rectangle(4, 2, 3, 1, 98).__str__(), value_needed)

    def str_str_test(self):
        value_needed = "change another value please!"
        self.assertEqual(str(Rectangle(4, 4)), value_needed)

    def str_str_method_with_args_test(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 4).__str__(42)


class Rectangle_update_with_args_test(TestCase):
    """New *args to the rectangle"""

    def init_base(self):
        Base._Base__nb_objects = 0

    def update_no_args_test(self):
        r = Rectangle(3, 5, 2, 3, 43)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (42) 1/2 - 2/4")

    def update_args_none_id_test(self):
        r = Rectangle(3, 5, 2, 3, 43)
        r.update(None)
        self.assertEqual(str(r), "[Rectangle] (1) 1/2 - 2/4")

    def update_args_id_test(self):
        r = Rectangle(3, 5, 2, 3, 43)
        r.update(24)
        self.assertEqual(str(r), "[Rectangle] (24) 1/2 - 2/4")

    def update_args_id_width_test(self):
        r = Rectangle(3, 5, 2, 3, 43)
        r.update(24, 10)
        self.assertEqual(str(r), "[Rectangle] (24) 1/2 - 10/4")

    def update_args_id_width_height_test(self):
        r = Rectangle(3, 5, 2, 3, 43)
        r.update(24, 10, 20)
        self.assertEqual(str(r), "[Rectangle] (24) 1/2 - 10/20")

    def update_args_id_width_height_x_test(self):
        r = Rectangle(3, 5, 2, 3, 43)
        r.update(24, 10, 20, 30)
        self.assertEqual(str(r), "[Rectangle] (24) 30/2 - 10/20")

    def update_args_id_width_height_x_y_test(self):
        r = Rectangle(3, 5, 2, 3, 43)
        r.update(24, 10, 20, 30, 40)
        self.assertEqual(str(r), "[Rectangle] (24) 30/40 - 10/20")

    def update_args_too_many_args_test(self):
        r = Rectangle(3, 5, 2, 3, 43)
        r.update(10, 10, 10, 10, 10, 50, 60)
        self.assertEqual(str(r), "[Rectangle] (10) 10/10 - 10/10")


class Rectangle_update_with_kwargs_test(TestCase):
    """New *args to the rectangle"""
    def init_base(self):
        Base._Base__nb_objects = 0

    def update_kwargs_none_id_test(self):
        r = Rectangle(3, 5, 2, 3, 43)
        r.update(id=None)
        self.assertEqual(str(r), "[Rectangle] (1) 1/2 - 2/4")

    def update_kwargs_id_test(self):
        r = Rectangle(3, 5, 2, 3, 43)
        r.update(id=24)
        self.assertEqual(str(r), "[Rectangle] (24) 1/2 - 2/4")

    def update_kwargs_id_width_test(self):
        r = Rectangle(3, 5, 2, 3, 43)
        r.update(width=10, id=24)
        self.assertEqual(str(r), "[Rectangle] (24) 1/2 - 10/4")

    def update_kwargs_id_width_height_test(self):
        r = Rectangle(3, 5, 2, 3, 43)
        r.update(width=10, id=24, height=20)
        self.assertEqual(str(r), "[Rectangle] (24) 1/2 - 10/20")

    def update_kwargs_id_width_height_x_test(self):
        r = Rectangle(3, 5, 2, 3, 43)
        r.update(width=10, id=24, x=30, height=20)
        self.assertEqual(str(r), "[Rectangle] (24) 30/2 - 10/20")

    def update_kwargs_id_width_height_x_y_test(self):
        r = Rectangle(3, 5, 2, 3, 43)
        r.update(y=40, width=10, id=24, x=30, height=20)
        self.assertEqual(str(r), "[Rectangle] (24) 30/40 - 10/20")

    def update_kwargs_too_many_args_test(self):
        r = Rectangle(3, 5, 2, 3, 43)
        r.update(y=10, width=10, id=10, x=10, height=10, alx="software")
        self.assertEqual(str(r), "[Rectangle] (10) 10/10 - 10/10")

    def update_kwargs_mixed_too_many_args_test(self):
        r = Rectangle(3, 5, 2, 3, 43)
        r.update(y=10, width=10, alx="software", id=10, x=10, height=10)
        self.assertEqual(str(r), "[Rectangle] (10) 10/10 - 10/10")

    def update_kwargs_args_before_test(self):
        r = Rectangle(3, 5, 2, 3, 43)
        r.update(42, 42, 42, y=10, x=10)
        self.assertEqual(str(r), "[Rectangle] (42) 1/2 - 42/42")

    def update_kwargs_not_all_mixed_test(self):
        r = Rectangle(3, 5, 2, 3, 43)
        r.update(y=10, x=10, height=10)
        self.assertEqual(str(r), "[Rectangle] (42) 10/10 - 2/10")

    def update_kwargs_only_wrong_keys_test(self):
        r = Rectangle(3, 5, 2, 3, 43)
        r.update(alx="software", software="alx")
        self.assertEqual(str(r), "[Rectangle] (42) 1/2 - 2/4")


class Rectangle_to_dict_test(TestCase):
    """to_dictionary method."""

    def to_dictionary_basic_test(self):
        r = Rectangle(3, 5, 2, 3, 43)
        value_needed = "change another value please!"
        self.assertDictEqual(r.to_dictionary(), value_needed)

    def to_dictionary_basic_with_args_test(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 4, 1, 2, 42).to_dictionary(42)


if __name__ == "__main__":
    unittest.main()
