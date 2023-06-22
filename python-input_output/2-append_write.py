#!/usr/bin/python3
"""Append write"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8) and
    returns the number of characters added
    """
    try:
        with open(filename, 'a', encoding='utf8') as file:
            file.write(text)
            return len(text)
    except FileNotFoundError:
        with open(filename, 'w', encoding='utf8') as file:
            file.write(text)
            return len(text)
