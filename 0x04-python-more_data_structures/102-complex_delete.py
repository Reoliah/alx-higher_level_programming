#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_keys = list(a_dictionary)

    for key_value in list_keys:
        if value == a_dictionary.get(key_value):
            del a_dictionary[key_value]

    return (a_dictionary)
