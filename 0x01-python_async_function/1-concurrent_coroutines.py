#!/usr/bin/env python3
"""Concurrent routines more about"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Creates tasks and awaits them

    Args:
        n: the number of tasks to create
        max_delay: maximum delay time between tasks
    Return:
        list: a list of floats that shows every delay before each task was executed
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
