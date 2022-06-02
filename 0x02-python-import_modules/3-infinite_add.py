#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total_sum = 0

    if len(sys.argv) == 1:
        print(0)

    elif len(sys.argv) == 2:
        x = int(sys.argv[1])
        print(x)

    elif len(sys.argv) > 2:
        for i in range(1, len(sys.argv)):
            total_sum = total_sum + int(sys.argv[i])
        print(total_sum)
