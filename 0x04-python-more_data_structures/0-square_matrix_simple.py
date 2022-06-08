#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix
    Args:
        matrix: 2-dimensional list
    Return: 2-D list same size as matrix
    """
    return [[i*i for i in row] for row in matrix]
