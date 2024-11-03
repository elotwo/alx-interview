#!/usr/bin/python3
"""
this script is utf-8 validation
"""


def validUTF8(data):
    """
    this code accept data
    """
    if not all(0 <= byte < 256 for byte in data):
        return False
    try:
        bytes(data).decode('utf-8')
        return True
    except UnicodeDecodeError:
        return False
