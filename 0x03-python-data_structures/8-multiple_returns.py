#!/usr/bin/python3


def multiple_returns(sentence):
    if sentence is not None:
        sen_length = len(sentence)
        if sen_length == 0:
            return (sen_length, None)
        return (sen_length, sentence[0])
