#!/usr/bin/env python3

import asyncio
from typing import List
async_generator = __import__('0-basic_async_syntax').async_generator

"""
import async_generator from the previous task
"""

async def async_comprehension() -> List[float]:
    """
    10 random numbers using the async_generator.

    Returns:
        List: 10 random numbers.
    """
    return [i async for i in async_generator()]
