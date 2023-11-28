#!/usr/bin/python3
"""Module conatining a function that multiplies 2 matrices using NumPy"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """Multiplies 2 matrices using NumPy

    Args:
        m_a: The first matrix
        m_b: The second matrix

    Returns:
        The multiplication of the two matrices
    """
    return numpy.matmul(m_a, m_b)
