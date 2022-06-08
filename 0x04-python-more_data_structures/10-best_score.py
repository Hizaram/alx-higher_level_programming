#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is not None:
        score = -99999
        stud = None
        for k in a_dictionary.keys():
            if a_dictionary[k] is None:
                return None
            if  a_dictionary[k] > score:
                score = a_dictionary[k]
                stud = k
            return stud
