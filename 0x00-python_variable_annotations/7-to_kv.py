#!/usr/bin/env python3
"""A type-annotated function to_kv"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    A function that takes a string k and
    an int OR float v as arguments and returns a tuple.
    """
    return (k, float(v**2))
