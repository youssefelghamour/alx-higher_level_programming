#!/usr/bin/python3
"""Square class"""


class Square:
    """defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Constructor

        Args:
            size: size of the square
        """
        self.size = size
        self.position = position

    def area(self):
        """Calculates the are of the square

        Returns:
            the area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """ Method to retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """returns the position value"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets the position value of the square"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or
                value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(0, self.size):
                for k in range(self.position[0]):
                    print(" ", end='')
                for j in range(self.size):
                    print("#", end='')
                print()
