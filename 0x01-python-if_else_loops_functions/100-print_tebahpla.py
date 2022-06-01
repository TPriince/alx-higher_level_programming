#!/usr/bin/python3
for i in reversed(range(97, 123)):
    if i % 2 == 1:
        print("{:s}".format(chr(i - 32)), end='')

    else:
        print("{:s}".format(chr(i)), end='')
