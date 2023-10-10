#!/usr/bin/env python3
"""
write a measure_runtime coroutine that will execute
async_comprehension four times in parallel using asyncio.gather.
"""
import asyncio
import time

from async_comprehensions import async_comprehension


async def measure_runtime() -> float:
    """
    This script imports the async_comprehension from
    async_comprehension file.
    It then uses asyncio.gather to execute asyns_comprehension
    four times concurrently.
    It measures the total runtime using time.time().
    Returns:
        The total runtime.
    """

    start_time = time.time()

    # Execute async_comprehension four times in parallel
    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
    )

    end_time = time.time()
    total_runtime = end_time - start_time

    return total_runtime
