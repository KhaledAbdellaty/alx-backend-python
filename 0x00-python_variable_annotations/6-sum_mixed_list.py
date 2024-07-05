#!/usr/bin/env python3
"""A type-annotated function sum_mixed_list"""
from typing import List, Union


def sum_list(mxd_list: List[Union[int, float]]) -> float:
    """
     A function which takes a mixed list mxd_list
     of floats as argument and returns their sum as a float.
    """
    return sum(mxd_list).__float__()
