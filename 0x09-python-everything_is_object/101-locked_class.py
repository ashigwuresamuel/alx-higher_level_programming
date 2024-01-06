#!/usr/bin/python3
"""Locked_Class Module"""


class LockedClass:
    """
    Class that stops the user from dynamically creating any new
    instance attributes, except if new attribute is called `first_name`
    """
    __slots__ = ('first_name')
    pass
