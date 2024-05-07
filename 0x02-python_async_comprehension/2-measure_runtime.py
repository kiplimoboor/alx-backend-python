#!/usr/bin/env python3
"""Runtime for this module"""


import asyncio
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the runtime for a coroutine
    Return:
        The runtime in seconds
    """

    for _ in range(4):
        tasks = asyncio.gather(async_comprehension())

    start = perf_counter()
    await tasks
    return (perf_counter()-start)
