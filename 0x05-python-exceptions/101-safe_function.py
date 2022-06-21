#!/usr/bin/python3
def safe_function(fct, *args):
    import sys

    try:
        return fct(*args)

    except (ValueError, ZeroDivisionError, TypeError, IndexError) as vzti:
        print("Exception: {}".format(vzti), file=sys.stderr)
        return None
