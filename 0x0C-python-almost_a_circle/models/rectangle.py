#!/usr/bin/python3
""" Module for Rectangle class """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor method """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ getter for width attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for width attribute """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ getter for height attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for height attribute """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ getter for the x attribute """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter for the x attribute """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ getter for the y attribute """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter for the y attribute """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
