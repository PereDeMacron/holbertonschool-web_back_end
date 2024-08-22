#!/usr/bin/env python3

import asyncio
import random
from typing import AsyncGenerator

"""
aynchronus generator
"""

async def async_generator() -> AsyncGenerator[float, None]:
    """
     random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
