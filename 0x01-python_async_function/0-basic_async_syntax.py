#!/usr/bin/env python3

"""Module with basics of async"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Delays for a maximum of max_delay second and returns the delay time

    Args:
        max_delay[int]: maximum time allowed for delay
    Return:
        float: the delay time of the function
    """

    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
