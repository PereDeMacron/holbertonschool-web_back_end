#!/usr/bin/env python3

import asyncio
import random
from typing import Generator

"""
aync_generator
"""

async def async_generator() -> Generator[float, None, None]:
    """
     aync_generator
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
