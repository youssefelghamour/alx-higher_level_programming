#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    """Suite test for max_integer function"""

    def test_basic(self):
        self.assertEqual(max_integer([8, 23, -6, 20, 99]), 99)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_no_argument(self):
        self.assertEqual(max_integer(), None)

    def test_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_repeated_number(self):
        self.assertEqual(max_integer([3, 2, 3]), 3)

    def test_negative(self):
        self.assertEqual(max_integer([-5, 2, 4]), 4)

    def test_float(self):
        self.assertEqual(max_integer([50, 51, 50, 49]), 51)

    def test_operation(self):
        self.assertEqual(max_integer([1, 5 * 2, 66]), 66)

    def test_zero_number(self):
        self.assertEqual(max_integer([0, 0]), 0)

    def test_big_list(self):
        self.assertEqual(max_integer([
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
            21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
            31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
            41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
            61, 62, 63, 64, 65, 66, 67, 68, 69, 60,
            71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
            81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
            91, 92, 93, 94, 95, 96, 97, 98, 99, 100]), 100)

    def test_list_with_loop(self):
        my_list = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer([i * 2 for i in my_list]), 10)

    def test_one_number_in_a_list(self):
        self.assertEqual(max_integer([1]), 1)

    def test_string_number_in_a_list(self):
        with self.assertRaises(TypeError):
            max_integer([0, '1'])

    def test_tuple_in_a_list(self):
        with self.assertRaises(TypeError):
            max_integer([10, (20, 30)])

    def test_dictionary(self):
        with self.assertRaises(KeyError):
            max_integer({'key1': 1, 'key2': 2})

    def test_number(self):
        with self.assertRaises(TypeError):
            max_integer(1)


if __name__ == '__main__':
    unittest.main()
