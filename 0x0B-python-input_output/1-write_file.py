#!/usr/bin/python3
""" Module that contains write_file function that writes into a file """


def write_file(filename="", text=""):
    """ Function that writes a string to a text file
        and returns the number of characters written

    Args:
        filename: name of the file
        text: text to write in the file

    Returns:
        the number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
