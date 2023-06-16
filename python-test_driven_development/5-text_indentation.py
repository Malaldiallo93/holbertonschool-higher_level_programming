#!/usr/bin/python3
"""Module that prints a text with 2 new lines after each
of these characters: ., ? and :
    Args:
        text (string): text to indent
"""


def text_indentation(text):
    """Function that prints a text with 2 new lines after each
    of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    for char in text:
        result += char
        if char in ['.', '?', ':']:
            result += "\n\n"

    print(result.strip())
