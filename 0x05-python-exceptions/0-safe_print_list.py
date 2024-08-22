#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Prints up to x elements of a list, safely.

    Args:
        my_list (list): The list from which to print elements.
        x (int): The number of elements to print.

    Returns:
        int: The number of elements actually printed.
    """
    count = 0  # Counter for the number of elements printed
    try:
        for i in range(x):  # Attempt to print each element up to x
            print(my_list[i], end="")  # Print element on the same line
            count += 1  # Increment counter for each printed element
    except IndexError:  # Handle case where x is larger than list length
        pass  # Do nothing if index is out of range
    print("")  # Print a newline after the list elements
    return count  # Return the total number of elements printed
