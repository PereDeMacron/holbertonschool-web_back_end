#!/usr/bin/env python3
"""Task 8"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by a given multiplier
    """
    def multiplier_function(number: float) -> float:
        return number * multiplier

    return multiplier_function
