#!/usr/bin/env python3
"""
This module implements the element_length function with a list of strings or
"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing the length of the elements of lst.

    Parameters:
        lst (Iterable[Sequence]): The list of strings or lists to process.

    Returns:
        list[tuple[Sequence, int]]: The list of tuples containing the length of
            the elements of lst.
    """
    return [(i, len(i)) for i in lst]
