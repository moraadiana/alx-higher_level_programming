#!/usr/bin/python3
"""add a new attr"""


def add_attribute(obj, name, value):

    if hasattr(obj, '__dict__') or name in getattr(obj, '__slots__', {}):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
