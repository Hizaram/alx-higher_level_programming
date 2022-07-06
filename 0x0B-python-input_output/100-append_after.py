#!/usr/bin/python3
"""Function that appends a line after a specified line is read
from a file"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts new_string in a file after search_string is found
    Args:
        filename (str): name of file
        search_string (str): required target string
        new_string (str): string to be appended
    """
    new_lines = []
    with open(filename, 'r+', encoding='utf-8') as f:
        for line in f:
            new_lines.append(line)
            if search_string in line:
                new_lines.append(new_string)
        for line in new_lines:
            f.write(line)
