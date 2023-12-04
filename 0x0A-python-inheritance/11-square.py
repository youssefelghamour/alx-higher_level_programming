#!/usr/bin/python3
""" Module for square class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class that inherits from Rectangle """

    def __init__(self, size):
        """ Method that initializes a Square """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """ Method that returns the area of the square """
        return self.__size ** 2

    def __str__(self):
        """ printable string method """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
