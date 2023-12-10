#!/usr/bin/python3
""" Module for Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor method """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ returns [Square] (<id>) <x>/<y> - <width>/<height> """
        str1 = "[Square]"
        str2 = " ({}) ".format(self.id)
        str3 = "{}/{} - ".format(self.x, self.y)
        str4 = "{}".format(self.width)
        return str1 + str2 + str3 + str4

    @property
    def size(self):
        """ getter for the size of the square """
        return self.width

    @size.setter
    def size(self, value):
        """ setter for the size of the square """
        self.width = value
        self.height = value
