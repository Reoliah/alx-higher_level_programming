#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = []
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        new_list = my_list.replace([0], '')
        return new_list
