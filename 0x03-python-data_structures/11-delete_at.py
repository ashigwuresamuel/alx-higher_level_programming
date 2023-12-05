#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    numb_element = len(my_list)
    if idx < 0:
        return my_list
    if idx >= numb_element:
        return my_list
    else:
        del my_list[idx]  # deletes the specified idx from list
    return my_list
