#!/usr/bin/env python3
"""
This module implements the to_kv function with a string k and an
integer or float v as arguments and returns a tuple.
The first element of the tuple is the string k. The second element
is the square of the int/float v and should be annotated as a float.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with the string k as its first element and the
    square of the int/float v as its second element.

    Parameters:
        k (str): The string to be returned in the first element of
            the tuple.
        v (Union[int, float]): The int/float to be squared and
            returned in the second element of the tuple.

    Returns:
        tuple[str, float]: The tuple with k as its first element and
            the square of v as its second element.
    """
    return (k, v * v)
