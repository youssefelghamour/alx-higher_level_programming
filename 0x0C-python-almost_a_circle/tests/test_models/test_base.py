#!/usr/bin/python3
""" Unittest for Base class """
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ Tests the Base class """

    def test_init_with_id(self):
        """ tests class with int id """
        b = Base(id=5)
        self.assertEqual(b.id, 5)

    def test_init_without_id(self):
        """ tests id incrementation """
        b1 = Base()
        b2 = Base()
        self.assertNotEqual(b1.id, b2.id)

    def test_init_id_increment(self):
        """ tests id incrementation """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_init_with_negative_id(self):
        """ tests class with a negative int id """
        b = Base(id=-5)
        self.assertEqual(b.id, -5)

    def test_init_with_zero_id(self):
        """ tests class with id = 0 """
        b = Base(0)
        self.assertEqual(b.id, 0)

    def test_init_with_float_id(self):
        """ tests class with a float id """
        b = Base(5.5)
        self.assertEqual(b.id, 5.5)

    def test_init_with_string_id(self):
        """ tests class with a string id """
        b = Base(id="hi")
        self.assertEqual(b.id, "hi")

    def test_init_dict_id(self):
        """ tests class with a dictionary id """
        b = Base({"hi": 123})
        self.assertEqual(b.id, {"hi": 123})

    def test_to_json_string(self):
        """ test to_json_string method """
        lst = [{'id': 2}, {'id': 7}]
        self.assertEqual(Base.to_json_string(lst), '[{"id": 2}, {"id": 7}]')

    def test_from_json_string(self):
        """ tests from_json_string method """
        b = Base.from_json_string('[{"id": 1}, {"id": 3}]')
        self.assertEqual(b, [{'id': 1}, {'id': 3}])


if __name__ == '__main__':
    unittest.main()
