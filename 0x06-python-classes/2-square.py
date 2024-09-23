#!/usr/bin/python3


"""Defines a class Square with size validation."""
class Square:
    """Represents a square with validated size."""

    def __init__(self, size=0):
        """Initialize a square with size validation."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
