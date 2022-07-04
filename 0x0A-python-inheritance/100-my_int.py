#!/usr/bin/python3
"""class MyInt that inherits from int"""


class MyInt(int):
    """rebel class of int"""

    def __eq__(self, n2):
        """Inverts the value of =="""
        return super().__ne__(n2)

    def __ne__(self, n2):
        """Inverts the value of !="""
        return super().__eq__(n2)
