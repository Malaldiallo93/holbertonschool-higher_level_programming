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

    separators = [".", "?", ":"]
    result = ""
    new_line = True

    for i in text:
        if new_line and i == " ":
            continue
        result += i
        if i in separators:
            result += "\n\n"
            new_line = True
        else:
            new_line = False

    print(result.strip(), end="")
