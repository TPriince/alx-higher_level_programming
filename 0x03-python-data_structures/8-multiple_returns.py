#!/usr/bin/python3
def multiple_returns(sentence):
    x = len(sentence)

    if len(sentence) == 0:
        y = None

    else:
        y = sentence[0]

    return (x, y)
