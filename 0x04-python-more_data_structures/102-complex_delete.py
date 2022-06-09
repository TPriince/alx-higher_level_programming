#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_of_keys = list(a_dictionary.keys())

    for i in list_of_keys:
        if value == a_dictionary[i]:
            del(a_dictionary[i])
    return a_dictionary
