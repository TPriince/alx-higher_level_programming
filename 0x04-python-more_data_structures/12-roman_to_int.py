#!/usr/bib/python3
def roman_to_int(roman_string):
    digits = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    prev = 0
    sum = 0

    for ch in roman_string:
        sum += digits[ch] if digits[ch] <= prev else digits[ch] - prev * 2
        prev = digits[ch]
    return sum
