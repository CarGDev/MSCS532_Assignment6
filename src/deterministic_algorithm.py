"""
Deterministic Selection Algorithm (Median of Medians)

This module implements the deterministic selection algorithm that finds the k-th
smallest element in an array in worst-case O(n) time using the Median of Medians
approach.

Author: Carlos Gutierrez
Course: MSCS532 - Data Structures and Algorithms
"""


def deterministic_select(arr: list, k: int, key=None) -> any:
    """
    Find the k-th smallest element in an array using deterministic selection
    (Median of Medians algorithm) in worst-case O(n) time.
    
    Args:
        arr: List of comparable elements
        k: The k-th smallest element to find (1-indexed, so k=1 is the minimum)
        key: Optional function to extract comparison key from elements
        
    Returns:
        The k-th smallest element in the array
        
    Raises:
        ValueError: If k is out of range [1, len(arr)]
        IndexError: If array is empty
        
    Examples:
        >>> arr = [3, 1, 4, 1, 5, 9, 2, 6]
        >>> deterministic_select(arr, 4)
        3
        >>> deterministic_select(arr, 1)
        1
        >>> deterministic_select(arr, len(arr))
        9
    """
    if not arr:
        raise IndexError("Cannot select from empty array")
    
    n = len(arr)
    if k < 1 or k > n:
        raise ValueError(f"k must be between 1 and {n}, got {k}")
    
    # Use key function if provided
    if key is None:
        key = lambda x: x
    
    # Create a copy to avoid modifying the original array
    arr_copy = list(arr)
    
    return _deterministic_select_recursive(arr_copy, 0, n - 1, k, key)


def _deterministic_select_recursive(arr: list, left: int, right: int, k: int, key) -> any:
    """
    Recursive helper function for deterministic selection.
    
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
    
    # Find a good pivot using median of medians
    pivot_index = _median_of_medians(arr, left, right, key)
    
    # Partition around the pivot
    pivot_index = _partition(arr, left, right, pivot_index, key)
    
    # Calculate the rank of the pivot in the current subarray
    rank = pivot_index - left + 1
    
    if k == rank:
        return arr[pivot_index]
    elif k < rank:
        return _deterministic_select_recursive(arr, left, pivot_index - 1, k, key)
    else:
        return _deterministic_select_recursive(arr, pivot_index + 1, right, k - rank, key)


def _median_of_medians(arr: list, left: int, right: int, key) -> int:
    """
    Find the median of medians to use as a good pivot.
    
    This function groups elements into groups of 5, finds the median of each
    group, then recursively finds the median of those medians.
    
    Args:
        arr: The array
        left: Left index of the subarray
        right: Right index of the subarray
        key: Function to extract comparison key
        
    Returns:
        Index of the median of medians element
    """
    n = right - left + 1
    
    # Base case: if n <= 5, just sort and return median
    if n <= 5:
        # Create indices list and sort by value
        indices = list(range(left, right + 1))
        indices.sort(key=lambda i: key(arr[i]))
        median_idx = indices[(n - 1) // 2]
        return median_idx
    
    # Divide into groups of 5 and find median of each
    medians = []
    for i in range(left, right + 1, 5):
        group_end = min(i + 4, right)
        group_indices = list(range(i, group_end + 1))
        group_indices.sort(key=lambda idx: key(arr[idx]))
        
        # Find median of this group
        median_index = group_indices[(len(group_indices) - 1) // 2]
        medians.append(median_index)
    
    # Recursively find the median of medians
    num_medians = len(medians)
    median_of_medians_rank = (num_medians + 1) // 2
    
    # Create a temporary array of median values
    median_values = [arr[idx] for idx in medians]
    median_values_copy = median_values.copy()
    
    # Find the median value
    median_value = _deterministic_select_recursive(
        median_values_copy, 0, len(median_values_copy) - 1, median_of_medians_rank, key
    )
    
    # Find the index of this median value in the original array
    for idx in medians:
        if arr[idx] == median_value:
            return idx
    
    # Fallback (should not reach here)
    return medians[len(medians) // 2]


def _partition(arr: list, left: int, right: int, pivot_index: int, key) -> int:
    """
    Partition the array around a pivot element.
    
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


def find_median(arr: list, key=None) -> any:
    """
    Find the median of an array using deterministic selection.
    
    Args:
        arr: List of comparable elements
        key: Optional function to extract comparison key
        
    Returns:
        The median element (or lower median if even number of elements)
        
    Examples:
        >>> find_median([3, 1, 4, 1, 5])
        3
        >>> find_median([3, 1, 4, 1, 5, 9])
        3
    """
    if not arr:
        raise ValueError("Cannot find median of empty array")
    
    n = len(arr)
    k = (n + 1) // 2  # Lower median for even-length arrays
    return deterministic_select(arr, k, key)

