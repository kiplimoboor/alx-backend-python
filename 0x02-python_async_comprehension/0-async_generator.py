#!/usr/bin/env python3
"""A coroutine called async_generator that takes no arguments"""

import asyncio
import random


async def async_generator():
    """
    A simple async generator
    Return:
        Yields a random number 10 times
    """
    i = 0
    while i < 10:
        i += 1
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
