#!/usr/bin/env python3
"""
Take the code from wait_n and alter it into
a new function task_wait_n
"""
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int):
    """
    Asynchronous coroutine that spawns task_wait_random
    n times with the specified max_delay and return the
    list of delays in ascending order.

    Args:
        n (int): The number of times to spawn task_wait_randon
        max_delay (int): The maximum delay in secoconds for
        call to task_wait_random

    Returns:
        List[float]: Alist of delays (float value) in ascending
        order.
    """

    delays = [(i, await task_wait_random(max_delay)) for i in range(n)]
    delays.sort(key=lambda x: x[0])
    return [delay for _, delay in delays]


if __name__ == "__main":
    print(asyncio.run(task_wait_n(5, 5)))
    print(asyncio.run(task_wait_n(10, 7)))
    print(asyncio.run(task_wait_n(10, 0)))
