#!/usr/bin/env python3
"""importing modules"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """asynchronous coroutine that take in an integer argument\
        (max_delay, with a default value of 10) named wait_random\
        that waits for a random delay between 0 and max_delay\
            (included and float value)
        seconds and eventually returns it
    """

    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
