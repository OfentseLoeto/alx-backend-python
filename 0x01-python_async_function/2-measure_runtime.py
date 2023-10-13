#!/usr/bin/env python3
"""
This function measures the total execution time
for wait_n(n, max_delay), and returns total_time / n.
"""
import asyncio
import time


from concurrent_coroutines import wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for
    wait_n(n, max_delay) and return total_time / n.

    Args:
        n (int): The number of times to call wait_n.
        max_delay (int): The maximum delay in seconds
        for each call to wait_n.

    Return:
          float: The average execution time per call.

    """
    # Recording the start time
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))

    # Recording the end time
    end_time = time.time()
    total_time = end_time - start_time

    return total_time / n

if __name__ == "__main__":
    n = 5
    max_delay = 9
    average_time = measure_time(n, max_delay)
    print(average_time)
