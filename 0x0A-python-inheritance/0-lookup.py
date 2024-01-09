#!/usr/bin/python3
"""
lockup object module
create a function that creates a prototype lookup(obj)
"""

def lookup(obj):
    """
    Functions that returna list of available attributes
    and list of an object.
    """
    return dir(obj)
