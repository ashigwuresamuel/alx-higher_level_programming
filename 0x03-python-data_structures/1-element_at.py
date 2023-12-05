#!/usr/bin/python3

def element_at(my_list, idx):
    # handle the case where the index (idx) is negative
    # equal to the number of elements in the lists.
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
