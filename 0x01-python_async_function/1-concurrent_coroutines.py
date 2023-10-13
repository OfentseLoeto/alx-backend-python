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
    delays = []
    tasks = []

    for i in range(n):
        task = wait_random(max_delay)
        tasks.append((i, task))

    for i, task in tasks:
        delay = await task
        delays.append((i, delay))

    sorted_delays = sorted(delays, key=lambda x: x[0])

    sorted_values = [delay for _, delay in sorted_delays]

    return sorted_values


if __name__ == "__main__":
    delays = asyncio.run(wait_n(5, 10))
    print(delays)
