#!/usr/bin/env python3
"""
This module implements the sum_mixed_list function with a list of
floats as arguments and returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list of integers and floats as a float.

    Parameters:
        mxd_lst (list[float]): The list of integers and floats to sum.

    Returns:
        float: The sum of the list of integers and floats.
    """
    return sum(mxd_lst)
