#!/usr/bin/env python3
"""The coroutine will loop 10 times"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Loops 10 time"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
