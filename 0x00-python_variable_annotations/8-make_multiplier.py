#!/usr/bin/env python3
"""Returning a function module"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    return lambda a: a * multiplier
