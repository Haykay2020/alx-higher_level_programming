#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """
    Prints all integers of a list
    Args:
        my_list: list of integers
    Return:
        None
    """
    for i in my_list:
        print("{:d}".format(i))
