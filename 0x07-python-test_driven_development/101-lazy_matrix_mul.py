#!/usr/bin/python3
"""
This module contains a function that multiplies 2 matrices using NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy.

    Args:
    m_a (list of lists): First matrix
    m_b (list of lists): Second matrix

    Returns:
    numpy.ndarray: Result of matrix multiplication

    Raises:
    ValueError: If matrices can't be multiplied
    """
    try:
        return np.matmul(m_a, m_b)
    except ValueError as e:
        raise ValueError("m_a and m_b can't be multiplied") from e
