#!/usr/bin/env python3
"""
This module defines an asynchronous coroutine wait_random
that waits for a random delay between 0 and max_delay seconds.
"""

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Asyncronous coroutine that waits for a random delay and retturn it.
    Args:
    max_delay (int, optional): The  maximum delay in seconds
    Returns:
    float: A random delay between 0 and max_delay(inclusive).
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay

if __name__ == "__main__":
    asyncio.run(wait_random())
