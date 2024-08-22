#!/usr/bin/python3
def safe_print_integer(value):
    """
    Safely prints an integer.

    Args:
        value: The value to be printed.

    Returns:
        bool: True if value was correctly printed as an integer, False otherwise.
    """
    try:
        print("{:d}".format(value))  # Attempt to format and print the value as an integer
        return True  # Return True if successful
    except (ValueError, TypeError):  # Handle cases where value is not an integer
        return False  # Return False if printing fails
