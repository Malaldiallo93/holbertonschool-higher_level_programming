#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """Function that returns a list of lists of integers
    representing the Pascal’s triangle of n"""
    triangle = []
    if n > 0:
        for i in range(n):
            n_list = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    n_list.append(1)
                else:
                    n_list.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            triangle.append(n_list)
    return triangle
