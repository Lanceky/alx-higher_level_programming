#!/usr/bin/python3
"""Defines a class Square with getters and setters."""


class Square:
    """Represents a square with size validation and getters/setters."""

    def __init__(self, size=0):
        """Initialize the square with size validation."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2
