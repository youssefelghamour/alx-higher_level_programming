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

    def update(self, *args, **kwargs):
        """ Updates the value of the attributes """
        if args:
            list = []
            for arg in args:
                list.append(arg)
            if len(list) > 0 and list[0] is not None:
                self.id = list[0]
            if len(list) > 1 and list[1] is not None:
                self.width = list[1]
                self.height = list[1]
            if len(list) > 2 and list[2] is not None:
                self.x = list[2]
            if len(list) > 3 and list[3] is not None:
                self.y = list[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.width = value
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """ returns the dictionary representation of a Square """
        return {"id": self.id, "x": self.x, "size": self.width, "y": self.y}
