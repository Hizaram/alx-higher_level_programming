#!/usr/bin/python3
"""Script that creates a class LockedClass""" 


class LockedClass:
    """LockedClass prevents dynamic creation of attributes other than
    `first_name`
    """
    __slots__ = ['first_name']
