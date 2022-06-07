#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """
    Deletes the item at a specific position in a list
    Args:
        my_list: list of integers
        idx: integer
    Return: list
    """
    if my_list and 0 <= idx < len(my_list):
        del my_list[idx]

    return my_list
