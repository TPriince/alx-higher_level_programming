#!/usr/bin/python3
def multiple_returns(sentence):
    x = len(sentence)
    y = sentence[0]

    if len(sentence) == 0:
        y = None
        z = (x, y)
        return z

    else:
        z = (x, y)
        return z
