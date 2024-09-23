#!/usr/bin/python3
"""
Module: 102-square.py
Defines the Square class representing a square with area-based comparison operators.
"""


class Square:
    """
    Represents a square.
    """
    def __init__(self, size=0):
        self.size = size

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
            value (int or float): The size value to be set.

        Raises:
            TypeError: If value is not a number (int or float).
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            float: The area of the square.
        """
        return self.size ** 2

    def __eq__(self, other):
        """
        Checks if two squares are equal based on area.

        Args:
            other (Square): The other square object to compare.

        Returns:
            bool: True if both squares have the same area, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Checks if two squares are not equal based on area.

        Args:
            other (Square): The other square object to compare.

        Returns:
            bool: True if both squares do not have the same area, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Checks if the current square is smaller than the other based on area.

        Args:
            other (Square): The other square object to compare.

        Returns:
            bool: True if the current square is smaller, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Checks if the current square is smaller than or equal to the other based on area.

        Args:
            other (Square): The other square object to compare.

        Returns:
            bool: True if the current square is smaller or equal, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Checks if the current square is greater than the other based on area.

        Args:
            other (Square): The other square object to compare.

        Returns:
            bool: True if the current square is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Checks if the current square is greater than or equal to the other based on area.

        Args:
            other (Square): The other square object to compare.

        Returns:
            bool: True if the current square is greater or equal, False otherwise.
        """
        return self.area() >= other.area()
