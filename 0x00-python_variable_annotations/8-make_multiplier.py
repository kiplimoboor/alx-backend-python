#!/usr/bin/env python3
"""Returning a function module"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a multiplier function

    Args:
        multiplier[float]: the multiplier
    Return:
        A function multiplying a float with multiplier
    """
    return lambda a: a * multiplier
