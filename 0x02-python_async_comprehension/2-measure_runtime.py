#!/usr/bin/env python3
"""
write a measure_runtime coroutine that will execute
async_comprehension four times in parallel using asyncio.gather.
"""
import asyncio
from typing import List


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


async def measure_runtime() -> float:
    """
    This script imports the async_comprehension from
    async_comprehension file.
    It then uses asyncio.gather to execute asyns_comprehension
    four times concurrently.
    It measures the total runtime using
    asyncio.get_event_loop().time()

    Returns:
        The total runtime.
    """

    start_time = asyncio.get_event_loop().time()

    # Execute async_comprehension four times in parallel
    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
    )

    end_time = asyncio.get_event_loop().time()
    total_runtime = end_time - start_time

    return total_runtime
