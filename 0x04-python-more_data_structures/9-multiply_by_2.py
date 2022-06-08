#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    if a_dictionary is not None:
        n_dict = dict(a_dictionary)
        for k, v in n_dict.items():
            n_dict[k] = v * 2

        return n_dict
