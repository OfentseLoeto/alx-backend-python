#!/usr/bin/env python3
"""
Write an async routine called wait_n that takes in
2 int arguments (in this order): n and max_delay
"""
import asyncio
from typing import List

# Import the wait_random coroutine from the previous file
from basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:

    """
    Asynchronous routine that spawns wait_random n times
    and returns the list of delays in ascending order.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The max delay in seconds for each call to wait_random.

    Returns:
        List[float]: A list of delays (float values) in ascending order
    """
    # Using asyncio.gather to run wait_dom n times
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)

    # Sort the list of delays
    delays.sort()

    return delays

if __name__ == "__main__":
    n = 5
    max_delay = 10
    print(asyncio.run(wait_n(n, max_delay)))
