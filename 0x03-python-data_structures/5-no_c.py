#!/usr/bin/python3

def no_c(my_string):
    # initialize an empty string new_string that will hold
    # the new version of your string.
    new_string = ""
    # loop through each character
    for char in my_string:
        if char.lower() not in ['c', 'C']:
            new_string += char
    # return the new string
    return new_string
