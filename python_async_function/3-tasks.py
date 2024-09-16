#!/usr/bin/env python3
"""Task 0"""


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """int max_delay returns asyncio.Task"""

    Tasks = asyncio.create_task(wait_random(max_delay))
    return Tasks
