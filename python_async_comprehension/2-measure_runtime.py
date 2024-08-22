#!/usr/bin/env python3
import asyncio
import time
from typing import List
async_comprehension = __import__('0-basic_async_syntax').async_comprehension

"""
import async_comprehension from the previous task
"""

async def measure_runtime() -> float:
    """
    Measure the total runtime of executing async_comprehension four times at same.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    return end_time - start_time
