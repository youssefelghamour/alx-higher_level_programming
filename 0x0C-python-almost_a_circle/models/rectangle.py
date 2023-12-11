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

    def area(self):
        """ Function that returns tha area of the rectangle """
        return self.height * self.width

    def display(self):
        """ Prints the Rectangle instance with the character # """
        y_axis = self.y * '\n'
        x_axis = self.x * ' '
        rectangle = y_axis + (x_axis + "#" * self.width + '\n') * self.height
        print(rectangle[:-1])

    def __str__(self):
        """ returns [Rectangle] (<id>) <x>/<y> - <width>/<height> """
        str1 = "[Rectangle]"
        str2 = " ({}) ".format(self.id)
        str3 = "{}/{} - ".format(self.x, self.y)
        str4 = "{}/{}".format(self.width, self.height)
        return str1 + str2 + str3 + str4

    def update(self, *args, **kwargs):
        """ Updates the value of the attributes """
        if args is not None and len(args) != 0:
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
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle """
        return {"x": self.__x, "y": self.__y, "id": self.id,
                "height": self.__height, "width": self.__width}
