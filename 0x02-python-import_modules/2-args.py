#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    counter = 0
    count = 0

    if len(sys.argv) == 1:
        print("{:d} arguments".format(0))

    elif len(sys.argv) == 2:
        print("{:d} argument:".format(1))
        print("{:d}: {}".format(1, sys.argv[1]))

    elif len(sys.argv) > 2:
        print("{:d} arguments:".format(len(sys.argv) - 1))
        for i in range(1, len(sys.argv)):
            counter = counter + 1
            count = count + 1
            print("{:d}: {}".format(counter, sys.argv[count]))
