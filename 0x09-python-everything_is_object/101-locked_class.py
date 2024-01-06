#!/usr/bin/python3
"""Locked Class Module"""


class LockedClass:
    """
    A Class that prevents the user from dynamically creating any new
    instance attributes, except if new attribute is called `first_name`
    """
    __orders__ = ('first_name')
    pass
