#!/usr/bin/env python3
""" 0. The basics of async"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Generates a random delay and then waits for that delay.

    Args:
        max_delay (int, optional): The max value of delay. Defaults to 10.

    Return: The random delay.
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
