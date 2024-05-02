#!/usr/bin/env python3
"""A module implementing list of floats"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sums a list of floats

    Args:
        input_list [list[float]]: a list of floats
    Return:
        Sum of the floats
    """
    return sum(input_list)
