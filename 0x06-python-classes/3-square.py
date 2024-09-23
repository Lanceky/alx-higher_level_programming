#!/usr/bin/python3
"""Defines a class Square with a method to calculate area."""


class Square:
    """Represents a square and can calculate its area."""

    def __init__(self, size=0):
        """Initialize the square with size validation."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2
