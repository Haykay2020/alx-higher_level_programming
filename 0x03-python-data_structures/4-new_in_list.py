#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
    Replaces an element in a list at a specific position
    without modifying the original list

    Args:
        my_list: list of integers
        idx: integer
        element: integer

    Return:
        List of integers
    """
    if (idx < 0 or idx >= len(my_list)):
        return my_list[:]

    return my_list[:idx] + [element] + my_list[idx + 1:]
