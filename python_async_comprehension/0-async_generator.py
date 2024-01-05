#!/usr/bin/env python3
"""Coroutine that takes no arguments"""
import asyncio
import random
from typing import Generator


async def async_generator(): #look no arguments
    """Coroutine that takes no arguments"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
