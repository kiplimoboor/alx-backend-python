#!/usr/bin/env python3
"""Wait time while running code"""

import asyncio
from time import perf_counter

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the time taken to complete an asyncio operation
    Args:
        n: number of tasks to handle
        max_delay: delay times between tasks
    Return:
        float: the amount of time taken per each task
    """
    start = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    return (perf_counter()-start) / n
