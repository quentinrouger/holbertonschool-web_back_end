#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""

import asyncio
import time
from typing import Generator, List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Run time for four parallel comprehensions"""
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end = time.perf_counter()
    return end - start
