"""
MSCS532 Assignment 6: Selection Algorithms and Data Structures

This package contains implementations of:
- Deterministic selection algorithm (Median of Medians)
- Randomized selection algorithm (Quickselect)
- Elementary data structures (Arrays, Stacks, Queues, Linked Lists, Trees)
"""

from .deterministic_algorithm import deterministic_select, find_median
from .randomized_algorithm import randomized_select, find_median as randomized_find_median
from .data_structures import (
    DynamicArray, Matrix, Stack, Queue, LinkedList, Tree, TreeNode
)

__all__ = [
    'deterministic_select',
    'find_median',
    'randomized_select',
    'randomized_find_median',
    'DynamicArray',
    'Matrix',
    'Stack',
    'Queue',
    'LinkedList',
    'Tree',
    'TreeNode',
]

