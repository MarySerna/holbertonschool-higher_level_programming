#!/usr/bin/python3
"""function that prints My name is <first name> <last name>
   arg:
       text(str): string

"""


def text_indentation(text):
    """Write a function that prints My name is <first name> <last name>
    Return: printed text
    """

    if text is None:
        return None
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for i in range(len(text)):
        if text[i] == ' ' and text[i + 1] == ' ':
            continue
        if text[i] is ' ' and text[i - 1] is '.':
            continue
        if text[i] is ' ' and text[i - 1] is '?':
            continue
        if text[i] is ' ' and text[i - 1] is ':':
            continue
        if text[i] is ' ' and text[i - 1] is ' ':
            continue
        print(text[i], end="")
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print()
            print()
