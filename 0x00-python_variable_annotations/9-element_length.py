#!/usr/bin/env python3
"""Duck typing implementation"""


from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Iterable[Sequence], int]]:
    """
    Takes in an iterable and finds the length of each item in iterable
    It stores the length and the specific item as a tuple
    Args: 
        lst [list]: a list of iterables
    Return:
        A list of tuples

    """
    return [(i, len(i)) for i in lst]
