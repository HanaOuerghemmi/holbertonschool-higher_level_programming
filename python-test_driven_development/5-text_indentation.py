#!/usr/bin/python3
"""text indentation"""


def text_indentation(text):
    """function that prints a text with 2 new lines after each of these characters: ., ? and :"""

    if not isinstance(text, str):
        raise TypeError(" ")

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] == "\n" or text[i] in ".?:":
            print("\n")
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
