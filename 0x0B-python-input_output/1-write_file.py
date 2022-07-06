#!/usr/bin/python3
"""Function that writes to a file"""


def write_file(filename="", text=""):
    """Writes text to the file and returns the number
    of characters written
    Args:
        filename (str): name of the file to be written to
        text (str): contents that are written
    Returns:
        Number of characters written
    """
    written_chars = 0
    with open(filename, 'w', encoding='utf-8') as f:
        written_chars += f.write(text)
    return written_chars
