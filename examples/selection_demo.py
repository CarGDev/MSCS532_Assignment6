"""
Demonstration of selection algorithms.

This script demonstrates the usage of deterministic and randomized selection
algorithms for finding the k-th smallest element in an array.

Author: Carlos Gutierrez
Course: MSCS532 - Data Structures and Algorithms
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.deterministic_algorithm import deterministic_select, find_median
from src.randomized_algorithm import randomized_select, find_median as rand_find_median


def demo_basic_selection():
    """Demonstrate basic selection operations."""
    print("=" * 60)
    print("Basic Selection Demo")
    print("=" * 60)
    
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(f"Array: {arr}")
    print()
    
    # Find various order statistics
    for k in [1, 3, 5, len(arr)]:
        det_result = deterministic_select(arr, k)
        rand_result = randomized_select(arr, k, seed=42)
        print(f"  {k}-th smallest element:")
        print(f"    Deterministic: {det_result}")
        print(f"    Randomized:    {rand_result}")
        print()
    
    # Find median
    print("Median:")
    print(f"  Deterministic: {find_median(arr)}")
    print(f"  Randomized:    {rand_find_median(arr, seed=42)}")
    print()


def demo_different_distributions():
    """Demonstrate selection on different input distributions."""
    print("=" * 60)
    print("Selection on Different Distributions")
    print("=" * 60)
    
    distributions = {
        "Sorted": list(range(1, 21)),
        "Reverse Sorted": list(range(20, 0, -1)),
        "Random": [3, 15, 7, 1, 19, 12, 8, 5, 14, 2, 10, 18, 6, 11, 4, 9, 16, 13, 17, 20],
        "With Duplicates": [5, 3, 5, 1, 3, 2, 5, 4, 3, 1, 2, 5, 4, 3, 2, 1, 5, 4, 3, 2]
    }
    
    k = 10  # Find 10th smallest
    
    for name, arr in distributions.items():
        print(f"\n{name} Array: {arr[:10]}..." if len(arr) > 10 else f"{name} Array: {arr}")
        det_result = deterministic_select(arr, k)
        rand_result = randomized_select(arr, k, seed=42)
        print(f"  {k}-th smallest:")
        print(f"    Deterministic: {det_result}")
        print(f"    Randomized:    {rand_result}")
    print()


def demo_median_finding():
    """Demonstrate median finding."""
    print("=" * 60)
    print("Median Finding Demo")
    print("=" * 60)
    
    test_arrays = [
        ([1, 2, 3, 4, 5], "Odd length"),
        ([1, 2, 3, 4, 5, 6], "Even length"),
        ([5, 2, 8, 1, 9, 3, 7, 4, 6], "Random order"),
        ([1, 1, 2, 2, 3, 3, 4, 4], "With duplicates")
    ]
    
    for arr, description in test_arrays:
        print(f"\n{description}: {arr}")
        det_median = find_median(arr)
        rand_median = rand_find_median(arr, seed=42)
        print(f"  Deterministic median: {det_median}")
        print(f"  Randomized median:    {rand_median}")
    print()


def demo_custom_key():
    """Demonstrate selection with custom key function."""
    print("=" * 60)
    print("Selection with Custom Key Function")
    print("=" * 60)
    
    # Array of dictionaries
    students = [
        {'name': 'Alice', 'score': 85},
        {'name': 'Bob', 'score': 92},
        {'name': 'Charlie', 'score': 78},
        {'name': 'Diana', 'score': 95},
        {'name': 'Eve', 'score': 88}
    ]
    
    print("Students:")
    for student in students:
        print(f"  {student['name']}: {student['score']}")
    print()
    
    # Find student with median score
    median_student = randomized_select(
        students, 
        (len(students) + 1) // 2,
        key=lambda x: x['score'],
        seed=42
    )
    print(f"Student with median score: {median_student['name']} ({median_student['score']})")
    print()


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("Selection Algorithms Demonstration")
    print("=" * 60 + "\n")
    
    demo_basic_selection()
    demo_different_distributions()
    demo_median_finding()
    demo_custom_key()
    
    print("=" * 60)
    print("Demo Complete!")
    print("=" * 60)

