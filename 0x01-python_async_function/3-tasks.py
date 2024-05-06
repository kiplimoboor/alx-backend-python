#!/usr/bin/env python3
"""A tasks module for alx assignment"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio task
    Args:
        max_delay: the delay time for tasks
    Return:
        An asyncio task
    """
    return asyncio.create_task(wait_random(max_delay))
