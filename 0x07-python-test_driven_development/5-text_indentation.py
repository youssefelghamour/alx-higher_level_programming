#!/usr/bin/python3
"""Module containing a function that prints 2 new lines after ".?:" """


def text_indentation(text):
    """ Function that prints a text with 2 new lines after each of
        these characters: ., ? and :

    Args:
        text: string

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".?:":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
