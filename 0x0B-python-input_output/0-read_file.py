#!/usr/bin/python3
""" Module that contains read_file function that reads from a file """


def read_file(filename=""):
    """ Function that reads a text file and prints it to stdout

    Args:
        filename: name of the file
    """
    file = open(filename, 'r', encoding="utf-8")
    data = file.read()
    print(data.strip())
    file.close()
