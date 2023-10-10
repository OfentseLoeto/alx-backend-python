#!/usr/bin/env python3
"""
A function that takes an integer and returns an asyncio.Task
"""
import asyncio
import random

from basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
     Create and return an asyncio.Task for wait_random
     with the given max_delay.

    Args:
        max_delay (int): The maximum delay in seconds for
        wait_random.

    Returns:
        asyncio.Task: An asyncio.Task representing the
        execution of wait_random.
    """
    loop = asyncio.get_event_loop()
    task = loop.create_task(wait_random(max_delay))

    return task
