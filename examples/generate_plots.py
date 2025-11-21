"""
Generate performance visualization plots for selection algorithms and data structures.

This script runs benchmarks and generates visualization plots comparing the
performance of deterministic and randomized selection algorithms, as well as
data structure operations.

Author: Carlos Gutierrez
Course: MSCS532 - Data Structures and Algorithms
"""

import sys
import os
import matplotlib.pyplot as plt
import numpy as np

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.benchmark import (
    generate_random_array,
    generate_sorted_array,
    generate_reverse_sorted_array,
    generate_nearly_sorted_array,
    generate_duplicate_heavy_array,
    benchmark_selection_algorithms,
    compare_stack_vs_list_push,
    compare_queue_vs_list,
    compare_linked_list_vs_list
)
from src.deterministic_algorithm import deterministic_select
from src.randomized_algorithm import randomized_select


def plot_selection_comparison():
    """Generate comparison plots for selection algorithms."""
    print("Generating selection algorithm comparison plots...")
    
    sizes = [100, 500, 1000, 2000, 5000]
    distributions = {
        'Random': generate_random_array,
        'Sorted': generate_sorted_array,
        'Reverse Sorted': generate_reverse_sorted_array,
        'Nearly Sorted': lambda n: generate_nearly_sorted_array(n, swaps=10, seed=42),
        'Many Duplicates': lambda n: generate_duplicate_heavy_array(n, unique_values=10, seed=42)
    }
    
    results = benchmark_selection_algorithms(sizes, distributions, iterations=3)
    
    # Plot 1: Line plot comparison
    plt.figure(figsize=(12, 8))
    for dist_name in distributions:
        det_times = results['deterministic'][dist_name]
        rand_times = results['randomized'][dist_name]
        
        # Filter out infinite times
        valid_sizes = [s for s, t in zip(sizes, det_times) if t != float('inf')]
        valid_det = [t for t in det_times if t != float('inf')]
        valid_rand = [t for s, t in zip(sizes, rand_times) if s in valid_sizes]
        
        if valid_sizes:
            plt.plot(valid_sizes, valid_det, marker='o', label=f'Deterministic ({dist_name})', linestyle='--')
            plt.plot(valid_sizes, valid_rand, marker='s', label=f'Randomized ({dist_name})', linestyle='-')
    
    plt.xlabel('Input Size (n)', fontsize=12)
    plt.ylabel('Execution Time (seconds)', fontsize=12)
    plt.title('Selection Algorithm Performance Comparison', fontsize=14, fontweight='bold')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, alpha=0.3)
    plt.yscale('log')
    plt.tight_layout()
    plt.savefig('docs/selection_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("  Saved: docs/selection_comparison.png")
    
    # Plot 2: Bar chart for specific size
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    test_size = 2000
    size_idx = sizes.index(test_size) if test_size in sizes else len(sizes) - 1
    
    dists = list(distributions.keys())
    det_heights = [results['deterministic'][d][size_idx] if results['deterministic'][d][size_idx] != float('inf') else 0 
                   for d in dists]
    rand_heights = [results['randomized'][d][size_idx] for d in dists]
    
    x = np.arange(len(dists))
    width = 0.35
    
    axes[0].bar(x - width/2, det_heights, width, label='Deterministic', alpha=0.8)
    axes[0].bar(x + width/2, rand_heights, width, label='Randomized', alpha=0.8)
    axes[0].set_xlabel('Distribution', fontsize=11)
    axes[0].set_ylabel('Execution Time (seconds)', fontsize=11)
    axes[0].set_title(f'Selection Performance at n={sizes[size_idx]}', fontsize=12, fontweight='bold')
    axes[0].set_xticks(x)
    axes[0].set_xticklabels(dists, rotation=45, ha='right')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3, axis='y')
    axes[0].set_yscale('log')
    
    # Scalability plot (random inputs only)
    random_sizes = sizes
    det_random = results['deterministic']['Random']
    rand_random = results['randomized']['Random']
    
    valid_sizes = [s for s, t in zip(random_sizes, det_random) if t != float('inf')]
    valid_det = [t for t in det_random if t != float('inf')]
    valid_rand = [t for s, t in zip(random_sizes, rand_random) if s in valid_sizes]
    
    axes[1].plot(valid_sizes, valid_det, marker='o', label='Deterministic', linewidth=2)
    axes[1].plot(valid_sizes, valid_rand, marker='s', label='Randomized', linewidth=2)
    
    # Reference line for O(n)
    if valid_sizes:
        ref_n = np.array(valid_sizes)
        ref_time = valid_det[0] * (ref_n / valid_sizes[0])
        axes[1].plot(ref_n, ref_time, '--', label='O(n) reference', alpha=0.5, color='gray')
    
    axes[1].set_xlabel('Input Size (n)', fontsize=11)
    axes[1].set_ylabel('Execution Time (seconds)', fontsize=11)
    axes[1].set_title('Scalability on Random Inputs', fontsize=12, fontweight='bold')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)
    axes[1].set_xscale('log')
    axes[1].set_yscale('log')
    
    plt.tight_layout()
    plt.savefig('docs/selection_bar_and_scalability.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("  Saved: docs/selection_bar_and_scalability.png")


def plot_data_structure_comparison():
    """Generate comparison plots for data structures."""
    print("Generating data structure comparison plots...")
    
    sizes = [100, 500, 1000, 2000, 5000]
    
    # Stack vs List
    stack_times = []
    list_times = []
    for size in sizes:
        result = compare_stack_vs_list_push(size, iterations=10)
        stack_times.append(result['stack'])
        list_times.append(result['list'])
    
    # Queue vs List
    queue_times = []
    list_enqueue_times = []
    for size in sizes:
        result = compare_queue_vs_list(size, iterations=10)
        queue_times.append(result['queue_enqueue'])
        list_enqueue_times.append(result['list_append'])
    
    # Linked List vs List
    ll_append_times = []
    ll_access_times = []
    list_append_times = []
    list_access_times = []
    for size in sizes:
        result = compare_linked_list_vs_list(size, iterations=10)
        ll_append_times.append(result['linked_list_append'])
        ll_access_times.append(result['linked_list_access'])
        list_append_times.append(result['list_append'])
        list_access_times.append(result['list_access'])
    
    # Plot 1: Stack vs List
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, stack_times, marker='o', label='Stack.push()', linewidth=2)
    plt.plot(sizes, list_times, marker='s', label='List.append()', linewidth=2)
    plt.xlabel('Number of Operations', fontsize=12)
    plt.ylabel('Total Time (seconds)', fontsize=12)
    plt.title('Stack vs List: Push/Append Performance', fontsize=14, fontweight='bold')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('docs/stack_vs_list.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("  Saved: docs/stack_vs_list.png")
    
    # Plot 2: Queue vs List
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, queue_times, marker='o', label='Queue.enqueue()', linewidth=2)
    plt.plot(sizes, list_enqueue_times, marker='s', label='List.append()', linewidth=2)
    plt.xlabel('Number of Operations', fontsize=12)
    plt.ylabel('Total Time (seconds)', fontsize=12)
    plt.title('Queue vs List: Enqueue/Append Performance', fontsize=14, fontweight='bold')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('docs/queue_vs_list.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("  Saved: docs/queue_vs_list.png")
    
    # Plot 3: Linked List vs List
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    axes[0].plot(sizes, ll_append_times, marker='o', label='LinkedList.append()', linewidth=2)
    axes[0].plot(sizes, list_append_times, marker='s', label='List.append()', linewidth=2)
    axes[0].set_xlabel('Number of Operations', fontsize=11)
    axes[0].set_ylabel('Total Time (seconds)', fontsize=11)
    axes[0].set_title('Append Operation', fontsize=12, fontweight='bold')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)
    
    axes[1].plot(sizes, ll_access_times, marker='o', label='LinkedList.get()', linewidth=2)
    axes[1].plot(sizes, list_access_times, marker='s', label='List[index]', linewidth=2)
    axes[1].set_xlabel('List Size', fontsize=11)
    axes[1].set_ylabel('Time per Access (seconds)', fontsize=11)
    axes[1].set_title('Access Operation', fontsize=12, fontweight='bold')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)
    axes[1].set_yscale('log')
    
    plt.suptitle('Linked List vs List Performance Comparison', fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig('docs/linked_list_vs_list.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("  Saved: docs/linked_list_vs_list.png")


if __name__ == "__main__":
    # Create docs directory if it doesn't exist
    os.makedirs('docs', exist_ok=True)
    
    print("\n" + "=" * 60)
    print("Generating Performance Visualization Plots")
    print("=" * 60 + "\n")
    
    try:
        plot_selection_comparison()
        print()
        plot_data_structure_comparison()
        print()
        print("=" * 60)
        print("All plots generated successfully!")
        print("=" * 60)
    except Exception as e:
        print(f"Error generating plots: {e}")
        import traceback
        traceback.print_exc()

