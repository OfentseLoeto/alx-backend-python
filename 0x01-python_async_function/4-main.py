#!/usr/bin/env python3
import asyncio

from tasks import task_wait_random

async def main():
    max_delay = 5
    num_tasks = 5
    tasks = [task_wait_random(max_delay) for _ in range(num_tasks)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
