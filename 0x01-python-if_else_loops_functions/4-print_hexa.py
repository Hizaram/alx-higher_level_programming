#!/usr/bin/python3


def get_hexa(number):
    hex_string = '0123456789abcdef'
    hex_tens = number // 16
    hex_units = number % 16
    if hex_tens > 0:
        return hex_string[hex_tens] + hex_string[hex_units]
    else:
        return hex_string[hex_units]


for number in range(99):
    print("{:d} = 0x{}".format(number, get_hexa(number)))
