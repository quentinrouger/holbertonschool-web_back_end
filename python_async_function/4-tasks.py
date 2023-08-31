#!/usr/bin/env python3
"""4. Tasks"""

from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.

    Args:
        n (int, optional): The number of times to spawn wait_random.
                            Defaults to 0.
        max_delay (int, optional): The max value of delay. Defaults to 10.

    Returns:
        list[float]: A list of all the delays.
    """
    delays = [await task_wait_random(max_delay) for _ in range(n)]
    return sorted(delays)

