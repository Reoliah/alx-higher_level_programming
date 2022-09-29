#!/usr/bin/python3
def best_score(a_dictionary):
    val = list(a_dictionary.values())
    key = list(a_dictionary)
    return (key[val.index(max(val))])
