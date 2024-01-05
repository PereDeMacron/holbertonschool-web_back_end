#!/usr/bin/env python3
"""Task 1"""


import asyncio
import random
import time
wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """returns a asyncio.Tasks"""

    Tasks = asyncio.create_task(wait_random(max_delay))
    return Tasks
