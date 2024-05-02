#!/usr/bin/env python3
"""Simple annotated function"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Creates a tuple

    Args:
        k[str]: the string that acts as a key
        v[int or float]: the value for the tuple
    Return:
        [tuple]: a tuple with the format (str, float)
    """
    return (k, v**2)
