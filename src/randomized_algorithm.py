"""
Randomized Selection Algorithm (Quickselect)

This module implements the randomized selection algorithm that finds the k-th
smallest element in an array in expected O(n) time using a randomized pivot
selection strategy.

Author: Carlos Gutierrez
Course: MSCS532 - Data Structures and Algorithms
"""

import random


def randomized_select(arr: list, k: int, key=None, seed=None) -> any:
    """
    Find the k-th smallest element in an array using randomized selection
    (Quickselect algorithm) in expected O(n) time.
    
    Args:
        arr: List of comparable elements
        k: The k-th smallest element to find (1-indexed, so k=1 is the minimum)
        key: Optional function to extract comparison key from elements
        seed: Optional random seed for reproducible results
        
    Returns:
        The k-th smallest element in the array
        
    Raises:
        ValueError: If k is out of range [1, len(arr)]
        IndexError: If array is empty
        
    Examples:
        >>> arr = [3, 1, 4, 1, 5, 9, 2, 6]
        >>> randomized_select(arr, 4, seed=42)
        3
        >>> randomized_select(arr, 1, seed=42)
        1
        >>> randomized_select(arr, len(arr), seed=42)
        9
    """
    if not arr:
        raise IndexError("Cannot select from empty array")
    
    n = len(arr)
    if k < 1 or k > n:
        raise ValueError(f"k must be between 1 and {n}, got {k}")
    
    # Set random seed if provided
    if seed is not None:
        random.seed(seed)
    
    # Use key function if provided
    if key is None:
        key = lambda x: x
    
    # Create a copy to avoid modifying the original array
    arr_copy = list(arr)
    
    return _randomized_select_recursive(arr_copy, 0, n - 1, k, key)


def _randomized_select_recursive(arr: list, left: int, right: int, k: int, key) -> any:
    """
    Recursive helper function for randomized selection.
    
    Args:
        arr: The array (will be modified during partitioning)
        left: Left index of the subarray
        right: Right index of the subarray
        k: The k-th smallest element to find (relative to left)
        key: Function to extract comparison key
        
    Returns:
        The k-th smallest element in arr[left:right+1]
    """
    if left == right:
        return arr[left]
    
    # Randomly select a pivot
    pivot_index = random.randint(left, right)
    
    # Partition around the pivot
    pivot_index = _partition(arr, left, right, pivot_index, key)
    
    # Calculate the rank of the pivot in the current subarray
    rank = pivot_index - left + 1
    
    if k == rank:
        return arr[pivot_index]
    elif k < rank:
        return _randomized_select_recursive(arr, left, pivot_index - 1, k, key)
    else:
        return _randomized_select_recursive(arr, pivot_index + 1, right, k - rank, key)


def _partition(arr: list, left: int, right: int, pivot_index: int, key) -> int:
    """
    Partition the array around a pivot element using Lomuto partition scheme.
    
    Elements less than the pivot go to the left, elements greater go to the right.
    The pivot is placed in its final sorted position.
    
    Args:
        arr: The array to partition
        left: Left index of the subarray
        right: Right index of the subarray
        pivot_index: Index of the pivot element
        key: Function to extract comparison key
        
    Returns:
        Final index of the pivot after partitioning
    """
    pivot_value = key(arr[pivot_index])
    
    # Move pivot to the end
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
    
    # Partition
    store_index = left
    for i in range(left, right):
        if key(arr[i]) < pivot_value:
            arr[store_index], arr[i] = arr[i], arr[store_index]
            store_index += 1
    
    # Move pivot to its final position
    arr[right], arr[store_index] = arr[store_index], arr[right]
    
    return store_index


def find_median(arr: list, key=None, seed=None) -> any:
    """
    Find the median of an array using randomized selection.
    
    Args:
        arr: List of comparable elements
        key: Optional function to extract comparison key
        seed: Optional random seed for reproducible results
        
    Returns:
        The median element (or lower median if even number of elements)
        
    Examples:
        >>> find_median([3, 1, 4, 1, 5], seed=42)
        3
        >>> find_median([3, 1, 4, 1, 5, 9], seed=42)
        3
    """
    if not arr:
        raise ValueError("Cannot find median of empty array")
    
    n = len(arr)
    k = (n + 1) // 2  # Lower median for even-length arrays
    return randomized_select(arr, k, key, seed)

