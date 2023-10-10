#!/usr/bin/env python3
"""
This function creates a coroutine called async_comprehension
that takes no arguments.

"""
import asyncio
import random
from typing import List

from async_generators import async_generator


async def async_comprehension() -> List[float]:
    """
    This function creates async_comprehension coroutine that
    collects collects 10 random numbers using an asynchronous
    comprehension over the async_generator coroutine

    Returns:
        A list of collected numbers.
    """

    collected_numbers = [i async for i in async_generator()]
    return collected_numbers
