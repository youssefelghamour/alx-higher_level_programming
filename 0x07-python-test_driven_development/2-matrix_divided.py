#!/usr/bin/python3
"""module contating a function that divides all the elements of a matrix"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): The input matrix containing integers or floats.
        div (int or float): The divisor to divide all elements of the matrix.

    Returns:
        A new matrix after division

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats,
                   if the divisor is not a number, or if each row of the matrix
                   does not have the same size.
        ZeroDivisionError: If the divisor is equal to zero.
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")

        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")

    return [[round(element / div, 2) for element in row] for row in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
