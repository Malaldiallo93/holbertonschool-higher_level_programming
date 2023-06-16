#!/usr/bin/python3
"""Module that prints a square with the character #
    Args:
        size (int): size length of the square
"""


def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
