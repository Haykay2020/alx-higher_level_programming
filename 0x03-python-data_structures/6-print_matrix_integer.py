#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers

    Args:
        matrix: list of lists of integers

    Return:
        None
    """
    if matrix:
        for row in matrix:
            n = len(row)
            for i in range(n):
                print("{:d}".format(row[i]), end=" " if i < n - 1 else "")
            print()
