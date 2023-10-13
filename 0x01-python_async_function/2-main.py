#!/usr/bin/env python3
import asyncio

measure_time = __import__('2-measure_runtime').measure_time


n = 5
max_delay = 9

async def main():
    result = await measure_time(n, max_delay)
    print(result)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
