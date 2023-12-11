#!/usr/bin/python3
""" unittest for Square class """
import unittest
from models.square import Square
from contextlib import redirect_stdout
import io


class TestSquareClass(unittest.TestCase):
    """ tests the Square class """

    def test_init_with_valid_values(self):
        """ tests attributes """
        square = Square(5, 2, 3, 1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 1)

    def test_init_with_negative_size(self):
        """ tests ValueError """
        with self.assertRaises(ValueError) as e:
            square = Square(-5, 2, 3, 1)
        msg = "width must be > 0"
        self.assertEqual(str(e.exception), msg)

    def test_init_with_non_integer_size(self):
        """ tests TypeError """
        with self.assertRaises(TypeError) as e:
            square = Square("5", 2, 3, 1)
        msg = "width must be an integer"
        self.assertEqual(str(e.exception), msg)

    def test_init_with_negative_x(self):
        """ tests ValueError for x """
        with self.assertRaises(ValueError) as e:
            square = Square(5, -2, 3, 1)
        msg = "x must be >= 0"
        self.assertEqual(str(e.exception), msg)

    def test_init_with_non_integer_x(self):
        """ tests TypeError for x """
        with self.assertRaises(TypeError) as e:
            square = Square(5, "2", 3, 1)
        msg = "x must be an integer"
        self.assertEqual(str(e.exception), msg)

    def test_display_method(self):
        """ tests the display method """
        s = Square(3, 2, 1, 1)
        f = io.StringIO()
        with redirect_stdout(f):
            s.display()
        output = "\n  ###\n  ###\n  ###\n"
        self.assertEqual(f.getvalue(), output)

    def test_size_property_setter(self):
        """ tests the updtae method """
        square = Square(5, 2, 3, 1)
        square.size = 8
        self.assertEqual(square.size, 8)
        self.assertEqual(square.width, 8)
        self.assertEqual(square.height, 8)

    def test_size_property_setter_with_negative_value(self):
        """ tests ValueError for size.setter """
        square = Square(5, 2, 3, 1)
        with self.assertRaises(ValueError) as e:
            square.size = -8
        msg = "width must be > 0"
        self.assertEqual(str(e.exception), msg)

    def test_size_property_setter_with_non_integer_value(self):
        """ tests TypeError for size.setter """
        square = Square(5, 2, 3, 1)
        with self.assertRaises(TypeError) as e:
            square.size = "8"
        msg = "width must be an integer"
        self.assertEqual(str(e.exception), msg)

    def test_str_representation(self):
        """ tests __str__ method """
        square = Square(5, 2, 3, 1)
        self.assertEqual(str(square), "[Square] (1) 2/3 - 5")

    def test_update_method_with_args(self):
        """ tests the update method width agrs """
        square = Square(5, 2, 3, 1)
        square.update(2, 8, 4, 6)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.width, 8)
        self.assertEqual(square.height, 8)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 6)

    def test_update_method_with_kwargs(self):
        """ tests the update method with kwargs """
        square = Square(5, 2, 3, 1)
        square.update(id=2, size=8, x=4, y=6)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.width, 8)
        self.assertEqual(square.height, 8)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 6)

    def test_to_dictionary_method(self):
        """ tests to_dictionary method """
        square = Square(5, 2, 3, 1)
        square_dict = square.to_dictionary()
        expected_dict = {"id": 1, "size": 5, "x": 2, "y": 3}
        self.assertDictEqual(square_dict, expected_dict)


if __name__ == '__main__':
    unittest.main()
