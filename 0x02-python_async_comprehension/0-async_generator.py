#!/usr/bin/env python3
"""A coroutine called async_generator that takes no arguments"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    A simple async generator
    Return:
        Yields a random number 10 times
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
