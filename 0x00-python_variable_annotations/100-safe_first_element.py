#!/usr/bin/env python3
"""A type-annotated function element_length"""
from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''Ryturn the first element of a sequence if it exists.'''
    if lst:
        return lst[0]
    else:
        return None
