#!/usr/bin/env python3
"""Simple int and float addition module"""

from typing import Union


def sum_mixed_list(mxd_list: Union[int, float]) -> float:
    return sum(mxd_list)
