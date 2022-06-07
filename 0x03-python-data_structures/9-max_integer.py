#!/usr/bin/python3

def max_integer(my_list=[]):
    """
    Finds the biggest integer of a list
    Args:
        my_list: list of integers
    Return: Integer
    """
    return (sorted(my_list)[-1] if (my_list and len(my_list)) else None)
