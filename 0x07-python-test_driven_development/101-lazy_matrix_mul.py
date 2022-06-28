#!/usr/bin/python3
"""
101-lazy_matrix_mul module
Matrix multiplication using NumPy.
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """Function that multiiplies m_a and m_b
    using matmul, and returns the result.
    """
    return numpy.matmul(m_a, m_b)
