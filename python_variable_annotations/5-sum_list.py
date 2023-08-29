#!/usr/bin/env python3
"""
This module implements the sum_list function with a list of floats
as arguments and returns their sum as a float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of floats as a float.

    Parameters:
        input_list (list[float]): The list of floats to sum.

    Returns:
        float: The sum of the list of floats.
    """
    return sum(input_list)
