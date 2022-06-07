#!/usr/bin/python3

def element_at(my_list, idx):
    """
    Retrieves a value from a list
    Args:
        my_list: list of integers
        idx: integer
    Return:
        Value at position idx in my_list. Otherwise None
    """
    return None if (idx < 0 or idx >= len(my_list)) else my_list[idx]
