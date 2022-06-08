#!/usr/bin/python3

def only_diff_elemets(set_1, set_2):
    """
    Creates a set of elements present in only one set

    Agrs:
        set_1: set
        set_2: set


    Return: set
    """

    return (set_1 - set_2) | (set_2 - set_1)
