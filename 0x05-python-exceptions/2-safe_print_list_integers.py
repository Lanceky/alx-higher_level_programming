#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of a list that are integers.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements to print.

    Returns:
        int: The number of integers printed.
    """
    count = 0  # Counter for the number of integers printed
    for i in range(x):  # Iterate through the list up to x elements
        try:
            print("{:d}".format(my_list[i]), end="")  # Print integer on the same line
            count += 1  # Increment counter for each printed integer
        except (ValueError, TypeError):  # Skip elements that are not integers
            continue  # Continue to the next element
    print("")  # Print a newline after the integers
    return count  # Return the total number of integers printed
