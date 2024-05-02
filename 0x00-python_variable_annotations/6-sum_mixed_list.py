#!/usr/bin/env python3
"""Simple int and float addition module"""

from typing import Union


def sum_mixed_list(mxd_list: Union[int, float]) -> float:
    """
    Adds a list of ints and floats

    Args:
        mxd_list[list]: a list of ints and floats
    Return:
        The sum of floats and ints in the mxd_list
    """
    return sum(mxd_list)
