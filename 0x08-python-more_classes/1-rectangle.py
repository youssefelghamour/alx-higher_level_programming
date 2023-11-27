#!/usr/bin/python3
""" Module for an empty Rectangle class """


class Rectangle:
    """ Rectangle class """

    def __init__(self, width=0, height=0):
        """ Method that initializes a rectangle

        Args:
            width: The width of the rectangle
            height: The height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter method that return the private attribute width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter method for the private attribute height

        Args:
            Value: the new width

        Raises:
            TypeError: if value is not an int
            ValueError: if value < 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter method that return the private attribute height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter method for the private attribute height

        Args:
            Value: the new height

        Raises:
            TypeError: if value is not an int
            ValueError: if value < 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
