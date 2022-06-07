#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """
    Finds all multiples of 2 in a list
    Args:
        my_list: list
    Return: list
    """
    return [i % 2 == 0 for i in my_list]
