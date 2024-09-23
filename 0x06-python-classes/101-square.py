#!/usr/bin/python3
"""
Module: 101-square.py
Defines the Square class representing a square.
"""

class Square:
    """
    Represents a square.
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The size value to be set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
            value (tuple): The position tuple (x, y).

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.size ** 2

    def my_print(self):
        """
        Prints the square with the character '#' on stdout.

        If size is 0, prints an empty line.
        """
        if self.size == 0:
            print("")
            return

        for _ in range(self.position[1]):
            print("")

        for _ in range(self.size):
            print(" " * self.position[0], end="")
            print("#" * self.size)

    def __str__(self):
        """
        Returns a string representation of the square (same as my_print).

        Returns:
            str: The string representation of the square.
        """
        return self.my_print()
