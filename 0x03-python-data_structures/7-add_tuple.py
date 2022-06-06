#!/usr/bin/python3


def tuple_conditions(tup):
    tup_length = len(tup)
    if tup_length == 0:
        return (0, 0)
    elif tup_length == 1:
        return (tup[0], 0)
    else:
        return (tup[0], tup[1])


def add_tuple(tuple_a=(), tuple_b=()):
    sum1 = 0
    sum2 = 0
    tup_a = tuple_conditions(tuple_a)
    tup_b = tuple_conditions(tuple_b)
    sum1 = tup_a[0] + tup_b[0]
    sum2 = tup_a[1] + tup_b[1]

    return (sum1, sum2)
