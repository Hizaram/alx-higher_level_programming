#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    updated_list = my_list[:]
    if idx < 0:
        return updated_list
    elif idx >= len(my_list):
        return updated_list
    else:
        updated_list[idx] = element
        return updated_list
