#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds key/value in a dictionary
    Args:
        a_dictionary: dictionary
        key: dictionary key
        value: value of key in the dictionary
    Return: dictionary
    """
    a_dictionary[key] = value
    return a_dictionary
