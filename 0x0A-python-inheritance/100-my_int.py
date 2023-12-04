#!/usr/bin/python3
""" Module for MyInt class """


class MyInt(int):
    """ Class that inherits from class int
        MyInt is a rebel. MyInt has == and != operators inverted
    """

    def __eq__(self, other):
        """ Method that turns == into != """
        return int(self) != other

    def __ne__(self, other):
        """ Method that turns != into == """
        return int(self) == other
