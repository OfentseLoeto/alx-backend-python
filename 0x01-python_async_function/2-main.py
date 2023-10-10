#!/usr/bin/env python3
import asyncio
measure_time = __import__('2-measure_runtime').measure_time


async def main():
    n = 5
    max_delay = 9
    average_time = await measure_time(n, max_delay)

    print(f"Average execution time per call: {average_time:.6f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
