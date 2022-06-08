#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list
    Args:
        my_list: integer list
    Return: integer
    """
    return sum(set(my_list))
