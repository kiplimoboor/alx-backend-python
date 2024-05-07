#!/usr/bin/env python3
"""Collect 10 random numbers using an"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronous for loop
    Return:
        list[float]: a list of floats yielded from async_generator
    """
    nums = [i async for i in async_generator()]
    return nums
