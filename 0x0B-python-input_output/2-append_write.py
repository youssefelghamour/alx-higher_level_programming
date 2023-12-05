#!/usr/bin/python3
""" Module that contains write_file function that appends text into a file """


def append_write(filename="", text=""):
    """ Function that appends a string at the end of a text file
        and returns the number of characters written

    Args:
        filename: name of the file
        text: text to append to the file

    Returns:
        the number of characters written
    """
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
