#!/usr/bin/env python3
"""Importing modules"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """an async routine called wait_n that
    take in 2 int arguments (in this order):
    n and max_delay
    spawn wait_random n times with the specified max_delay
    return the list of all the delays (float values)
    """

    wait_times = await asyncio.gather(*(wait_random(max_delay)
                                        for _ in range(n)))
    return sorted(wait_times)
