#!/usr/bin/python3
""" Module for append_after function """


def append_after(filename="", search_string="", new_string=""):
    """ Function that inserts a line of text to a file,
        after each line containing a specific string

    Args:
        filename: filename
        search_string: string to search
        new_string: string to append
    """

    lines = []
    with open(filename, 'r', encoding="utf-8") as file:
        for line in file:
            lines += [line]
            if search_string in line:
                lines.append(new_string)

    with open(filename, 'w', encoding="utf-8") as file:
        file.writelines(lines)
