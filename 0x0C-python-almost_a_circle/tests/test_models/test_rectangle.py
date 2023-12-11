#!/usr/bin/python3
""" Unittest for Rectangle class """
import unittest
from models.rectangle import Rectangle
from contextlib import redirect_stdout
import io


class TestRectangleClass(unittest.TestCase):
    """ tests the Rectangle class """

    def test_init_with_valid_values(self):
        """ tests attributes """
        rect = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)
        self.assertEqual(rect.id, 1)

    def test_init_with_negative_width(self):
        """ tests ValueError """
        rect = Rectangle(-5, 10, 2, 3, 1)
        self.assertRaises(ValueError)

    def test_init_with_non_integer_width(self):
        """ tests TypeError """
        rect = Rectangle("5", 10, 2, 3, 1)
        self.assertRaises(TypeError)

    def test_area_calculation(self):
        """ test the area method """
        rect = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(rect.area(), 50)

    def test_display_method(self):
        """ tests the display method """
        r = Rectangle(5, 2)
        r.width = 3
        r.height = 5
        f = io.StringIO()
        with redirect_stdout(f):
            r.display()
        s = "###\n###\n###\n###\n###\n"
        self.assertEqual(f.getvalue(), s)

    def test_str_representation(self):
        """ tests __str__ method """
        rect = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(str(rect), "[Rectangle] (1) 2/3 - 5/10")

    def test_update_method_with_args(self):
        """ tests the update method """
        rect = Rectangle(5, 10, 2, 3, 1)
        rect.update(2, 8, 12, 4, 6)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 8)
        self.assertEqual(rect.height, 12)
        self.assertEqual(rect.x, 4)
        self.assertEqual(rect.y, 6)

    def test_update_method_with_kwargs(self):
        """ tests the update method with **kwargs """
        rect = Rectangle(5, 10, 2, 3, 1)
        rect.update(id=2, width=8, height=12, x=4, y=6)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 8)
        self.assertEqual(rect.height, 12)
        self.assertEqual(rect.x, 4)
        self.assertEqual(rect.y, 6)

    def test_to_dictionary_method(self):
        """ tests the to_dictionary method """
        rect = Rectangle(5, 10, 2, 3, 1)
        rect_dict = rect.to_dictionary()
        expected_dict = {"id": 1, "width": 5, "height": 10, "x": 2, "y": 3}
        self.assertDictEqual(rect_dict, expected_dict)


if __name__ == "__main__":
    unittest.main()
