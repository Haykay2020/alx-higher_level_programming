#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    Replaces an element of a list at a specific position
    Args:
        my_list: list of integers
        idx: integer
        element: integer
    Return:
        List of integers
    """
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element

    return my_list
