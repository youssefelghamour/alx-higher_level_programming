#!/usr/bin/python3
""" Module for BaseGeometry class """


class BaseGeometry():
    """ BaseGeometry class """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Method that validates value

        Args:
            name: string
            value: int value

        Raises:
            TypeError: if value is not an integer
            ValueError: if value <= 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
