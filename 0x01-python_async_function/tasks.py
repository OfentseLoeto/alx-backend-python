#!/usr/bin/env python3
"""
Take the code from wait_n and alter it into
a new function task_wait_n
"""
import asyncio
from typing import List
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between
    0 and max_delay seconds and return it.

    Args:
        max_delay(int, optional): The max delay in seconds.
        Defaults 10.

    Returns:
        float: The random delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return asyncio.Task for wait random with the 
    given max_delay.

    Args:
         max_delay (int, optional): maximum delay in seconds for
         wait_random.

    Returns:
         asyncio.Task: An asyncio.Task representing the execution
         of wait_random.
    """
    loop = asyncio.get_event_loop()
    task = loop.create_task(wait_random(max_delay))
    return task



async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns task_wait_random n times 
    with the specified max_delay and return the list of delays
    in ascending order.

    Args:
        n (int): The number of times to spawn task_wait_randon
        max_delay (int): The maximum delay in secoconds for
        call to task_wait_random

    Returns:
        List[float]: Alist of delays (float value) in ascending                     order.
    """

    delays = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays

if __name__ == "__main__":
    n = 5
    max_delay = 10
    delays = asyncio.run(task_wait_n(n, max_delay))
    print(delays)
