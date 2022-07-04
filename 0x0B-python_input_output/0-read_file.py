#!/usr/bin/python3
"""Function that reads a text file"""


def read_file(filename=""):
    """Reads a text file and prints the contents to stdout
    Args:
        filename (str): name of the text file to be read
    """
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
