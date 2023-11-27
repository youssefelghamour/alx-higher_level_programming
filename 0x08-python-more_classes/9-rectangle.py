#!/usr/bin/python3
""" Module for an empty Rectangle class """


class Rectangle:
    """ Rectangle class """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Method that initializes a rectangle

        Args:
            width: The width of the rectangle
            height: The height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ Method that returns the rectangle area """
        return self.__height * self.__width

    def perimeter(self):
        """ Method that returns the rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0

        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """ Method that returns a string represetation of the rectangle using
            the character '#'
        """
        rectangle = ""

        if self.__height == 0 or self.__width == 0:
            return rectangle

        for i in range(self.__height):
            for j in range(self.__width):
                rectangle += str(self.print_symbol)
            rectangle += "\n"

        return rectangle[:-1]

    def __repr__(self):
        """ Method that returns a string representation of the rectangle """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ Method that Print the message "Bye rectangle..."
            when an instance of Rectangle is deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """ Method that returns the biggest rectangle based on the area

        Args:
            rect_1: The first rectangle
            rect_2: The second rectangle

        Raises:
            TypeError: if one of the rectangles is not an instance of
                        the Rectangle class

        Returns: the bigger rectangle
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ Class method that returns a square

        Args:
            cls: Rectangle class
            size: The size of the square (width = height = size)

        Returns:
            Instanse of the Rectangle class
        """

        return cls(size, size)
