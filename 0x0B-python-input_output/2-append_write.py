#!/usr/bin/python3
"""Function that appends text to a file"""


def append_write(filename="", text=""):
    """Appends the contents of text to file
    Args:
        filename (str): name of the file
        text (str): text to be appended
    Returns:
        number of characters added
    """
    chars_appended = 0
    with open(filename, 'a', encoding='utf-8') as f:
        chars_appended += f.write(text)
    return chars_appended
