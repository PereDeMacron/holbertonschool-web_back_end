#!/usr/bin/env python3
"""Task 9"""

from typing import List, Tuple, Union, Callable, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in the list
    """
    return [(i, len(i)) for i in lst]
