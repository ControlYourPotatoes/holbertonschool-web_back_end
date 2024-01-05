#!/usr/bin/env python3
"""measure the runtime"""
import time
import asyncio
from typing import List
from importlib import import_module

# Importing the wait_n function dynamically
module_name = '1-concurrent_coroutines'
module = import_module(module_name)
wait_n = module.wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average execution time for wait_n(n, max_delay).
    """
    start_time = time.time()

    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()
    total_time = end_time - start_time

    return total_time / n
