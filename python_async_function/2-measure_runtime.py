#!/usr/bin/env python3
"""2. Measure the runtime"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time for wait_n(n, max_delay).

    Args:
        n (int): The number of times to execute wait_random.
        max_delay (int): The max value of delay.

    Returns:
        float: The total execution time for wait_n(n, max_delay).
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
