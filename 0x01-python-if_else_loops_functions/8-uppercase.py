#!/usr/bin/python3
def uppercase(str):
    word = ""
    for i in str:
        if ord(i) in range(97, 123):
            word += chr(ord(i) - 32)

        else:
            word += i

    print("{:s}".format(word))
