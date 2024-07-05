#!/usr/bin/env python3
"""A type-annotated function element_length"""
from typing import Tuple, Iterable, List, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    A function that take lst as argument
    and return tuble of element and the element length
    """
    return [(i, len(i)) for i in lst]
