#!/usr/bin/python3
"""
Module that defines minOperations function.
"""


def minOperations(n):
    """
    Calculate the minimum number of operations needed
    to achieve n H characters starting with one H.

    Operations:
    - Copy All (Ctrl+A, Ctrl+C)
    - Paste (Ctrl+V)
    Args:
        n (int): The target number of H characters.
    Returns:
        int: Minimum number of operations, or 0 if n is less than 2.
    """
    if n < 2:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
