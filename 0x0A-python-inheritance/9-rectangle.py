#!/usr/bin/python3
""" Module for Rectangle class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class that inherits from BaseGeometry Class """

    def __init__(self, width, height):
        """ Constructor method """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Method that returns the area of the rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ printable string method """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
