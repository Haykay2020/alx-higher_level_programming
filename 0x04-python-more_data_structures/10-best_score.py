#!/usr/bin/python3

def best_score(a_dictionary):
    """
    Finds a key with the biggest integer value

    Args:
        a_dictionary: dictionary

    Return: key with biggest integer value. Otherwis NULL
    """

    if (a_dictionary and len(a_dictionary)):
        return max(a_dictionary, key=a_dictionary.get)

    return None
