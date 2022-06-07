#!/usr/bin/python3

def multiple_returns(sentence):
    """
    Creates a tuple with the length of a string and its first character

    Args:
        sentence: string

    Return:
        Tuple
    """
    return (len(sentence), sentence[0] if len(sentence) else None)
