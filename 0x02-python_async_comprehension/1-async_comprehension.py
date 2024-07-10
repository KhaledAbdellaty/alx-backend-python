#!/usr/bin/env python3
"""An asynchronous coroutine """
async_generator = __import__("0-async_generator").async_generator
from typing import List


async def async_comprehension() -> List[float]:
    """A function that  collect 10 random numbers
    using an async comprehensing over async_generator"""
    return [i async for i in async_generator()]
