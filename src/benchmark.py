"""
Benchmarking utilities for selection algorithms and data structures.

This module provides functions to generate test data and benchmark the performance
of selection algorithms and data structure operations.

Author: Carlos Gutierrez
Course: MSCS532 - Data Structures and Algorithms
"""

import time
import numpy as np
from typing import List, Dict, Tuple, Callable, Any

# Use try/except to support both relative and absolute imports
try:
    from .deterministic_algorithm import deterministic_select
    from .randomized_algorithm import randomized_select
except ImportError:
    from src.deterministic_algorithm import deterministic_select
    from src.randomized_algorithm import randomized_select


def generate_random_array(n: int, seed: int = None) -> List[int]:
    """Generate a random array of n integers."""
    if seed is not None:
        np.random.seed(seed)
    return np.random.randint(1, 1000, size=n).tolist()


def generate_sorted_array(n: int) -> List[int]:
    """Generate a sorted array of n integers."""
    return list(range(1, n + 1))


def generate_reverse_sorted_array(n: int) -> List[int]:
    """Generate a reverse-sorted array of n integers."""
    return list(range(n, 0, -1))


def generate_nearly_sorted_array(n: int, swaps: int = 10, seed: int = None) -> List[int]:
    """Generate a nearly sorted array with a few swaps."""
    arr = generate_sorted_array(n)
    if seed is not None:
        np.random.seed(seed)
    for _ in range(swaps):
        i, j = np.random.randint(0, n, size=2)
        arr[i], arr[j] = arr[j], arr[i]
    return arr


def generate_duplicate_heavy_array(n: int, unique_values: int = 10, seed: int = None) -> List[int]:
    """Generate an array with many duplicate values."""
    if seed is not None:
        np.random.seed(seed)
    values = np.random.randint(1, 1000, size=unique_values).tolist()
    return np.random.choice(values, size=n).tolist()


def benchmark_selection(
    algorithm: Callable,
    arr: List[int],
    k: int,
    iterations: int = 3,
    seed: int = None
) -> Tuple[float, Any]:
    """
    Benchmark a selection algorithm.
    
    Args:
        algorithm: The selection function to benchmark
        arr: Input array
        k: The k-th smallest element to find
        iterations: Number of iterations to average
        seed: Random seed for reproducibility
        
    Returns:
        Tuple of (average_time_seconds, result_value)
    """
    times = []
    result = None
    
    for i in range(iterations):
        arr_copy = list(arr)  # Fresh copy for each iteration
        
        start = time.perf_counter()
        if seed is not None:
            result = algorithm(arr_copy, k, seed=seed + i)
        else:
            result = algorithm(arr_copy, k)
        end = time.perf_counter()
        
        times.append(end - start)
    
    avg_time = sum(times) / len(times)
    return avg_time, result


def benchmark_selection_algorithms(
    sizes: List[int],
    distributions: Dict[str, Callable],
    k_ratios: List[float] = [0.25, 0.5, 0.75],
    iterations: int = 3
) -> Dict[str, Dict[str, List[float]]]:
    """
    Benchmark both deterministic and randomized selection algorithms.
    
    Args:
        sizes: List of input sizes to test
        distributions: Dictionary mapping distribution names to generator functions
        k_ratios: List of ratios to determine k (k = ratio * n)
        iterations: Number of iterations per benchmark
        
    Returns:
        Dictionary with benchmark results
    """
    results = {
        'deterministic': {dist: [] for dist in distributions},
        'randomized': {dist: [] for dist in distributions}
    }
    
    for size in sizes:
        print(f"Benchmarking size {size}...")
        
        for dist_name, dist_func in distributions.items():
            # Generate test array
            arr = dist_func(size)
            
            # Test different k values
            k_values = [max(1, int(ratio * size)) for ratio in k_ratios]
            k = k_values[len(k_values) // 2]  # Use middle k value
            
            # Benchmark deterministic
            try:
                time_det, _ = benchmark_selection(
                    deterministic_select, arr, k, iterations
                )
                results['deterministic'][dist_name].append(time_det)
            except (RecursionError, Exception) as e:
                print(f"  Deterministic failed for {dist_name} at size {size}: {e}")
                results['deterministic'][dist_name].append(float('inf'))
            
            # Benchmark randomized
            try:
                time_rand, _ = benchmark_selection(
                    randomized_select, arr, k, iterations, seed=42
                )
                results['randomized'][dist_name].append(time_rand)
            except (RecursionError, Exception) as e:
                print(f"  Randomized failed for {dist_name} at size {size}: {e}")
                results['randomized'][dist_name].append(float('inf'))
    
    return results


def benchmark_data_structure_operation(
    operation: Callable,
    iterations: int = 1000
) -> float:
    """
    Benchmark a data structure operation.
    
    Args:
        operation: Function that performs the operation
        iterations: Number of iterations
        
    Returns:
        Average time per operation in seconds
    """
    times = []
    for _ in range(iterations):
        start = time.perf_counter()
        operation()
        end = time.perf_counter()
        times.append(end - start)
    
    return sum(times) / len(times)


def compare_stack_vs_list_push(n: int, iterations: int = 10) -> Dict[str, float]:
    """Compare stack push operation vs list append."""
    try:
        from .data_structures import Stack
    except ImportError:
        from src.data_structures import Stack
    
    # Benchmark Stack
    stack_times = []
    for _ in range(iterations):
        stack = Stack()
        start = time.perf_counter()
        for i in range(n):
            stack.push(i)
        end = time.perf_counter()
        stack_times.append(end - start)
    
    # Benchmark List
    list_times = []
    for _ in range(iterations):
        lst = []
        start = time.perf_counter()
        for i in range(n):
            lst.append(i)
        end = time.perf_counter()
        list_times.append(end - start)
    
    return {
        'stack': sum(stack_times) / len(stack_times),
        'list': sum(list_times) / len(list_times)
    }


def compare_queue_vs_list(n: int, iterations: int = 10) -> Dict[str, float]:
    """Compare queue operations vs list operations."""
    try:
        from .data_structures import Queue
    except ImportError:
        from src.data_structures import Queue
    
    # Benchmark Queue enqueue
    queue_times = []
    for _ in range(iterations):
        queue = Queue()
        start = time.perf_counter()
        for i in range(n):
            queue.enqueue(i)
        end = time.perf_counter()
        queue_times.append(end - start)
    
    # Benchmark List append
    list_times = []
    for _ in range(iterations):
        lst = []
        start = time.perf_counter()
        for i in range(n):
            lst.append(i)
        end = time.perf_counter()
        list_times.append(end - start)
    
    return {
        'queue_enqueue': sum(queue_times) / len(queue_times),
        'list_append': sum(list_times) / len(list_times)
    }


def compare_linked_list_vs_list(n: int, iterations: int = 10) -> Dict[str, float]:
    """Compare linked list operations vs list operations."""
    try:
        from .data_structures import LinkedList
    except ImportError:
        from src.data_structures import LinkedList
    
    # Benchmark LinkedList append
    ll_times = []
    for _ in range(iterations):
        ll = LinkedList()
        start = time.perf_counter()
        for i in range(n):
            ll.append(i)
        end = time.perf_counter()
        ll_times.append(end - start)
    
    # Benchmark List append
    list_times = []
    for _ in range(iterations):
        lst = []
        start = time.perf_counter()
        for i in range(n):
            lst.append(i)
        end = time.perf_counter()
        list_times.append(end - start)
    
    # Benchmark LinkedList access
    ll = LinkedList()
    for i in range(n):
        ll.append(i)
    
    ll_access_times = []
    for _ in range(iterations):
        start = time.perf_counter()
        _ = ll.get(n // 2)
        end = time.perf_counter()
        ll_access_times.append(end - start)
    
    # Benchmark List access
    lst = list(range(n))
    list_access_times = []
    for _ in range(iterations):
        start = time.perf_counter()
        _ = lst[n // 2]
        end = time.perf_counter()
        list_access_times.append(end - start)
    
    return {
        'linked_list_append': sum(ll_times) / len(ll_times),
        'list_append': sum(list_times) / len(list_times),
        'linked_list_access': sum(ll_access_times) / len(ll_access_times),
        'list_access': sum(list_access_times) / len(list_access_times)
    }

