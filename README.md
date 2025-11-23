# MSCS532 Assignment 6: Medians and Order Statistics & Elementary Data Structures

**Author:** Carlos Gutierrez  
**Email:** cgutierrez44833@ucumberlands.edu  
**Course:** MSCS532 – Data Structures and Algorithms  
**Assignment:** Medians and Order Statistics & Elementary Data Structures

## What This Repository Contains

This repository contains all code, analysis, benchmarks, visualizations, and documentation required for Assignment 6. It includes both deterministic and randomized selection algorithms, complete data structure implementations, and a full empirical and theoretical analysis. All implementations were developed from scratch with comprehensive testing and validation.

**Full detailed analysis is available in [REPORT.md](REPORT.md).**

## Overview

This assignment delivers a comprehensive study of selection algorithms (finding the k-th smallest element) and elementary data structures. It includes deterministic and randomized selection implementations, complete data structure implementations (arrays, stacks, queues, linked lists, and trees), theoretical complexity analysis, empirical benchmarking, test coverage, and reproducible visualization assets.

## Repository Structure

```
MSCS532_Assignment6/
├── docs/
│   ├── selection_comparison.png              # Selection algorithm performance comparison
│   ├── selection_bar_and_scalability.png    # Bar chart and scalability analysis
│   ├── stack_vs_list.png                     # Stack vs List performance
│   ├── queue_vs_list.png                     # Queue vs List performance
│   └── linked_list_vs_list.png               # Linked List vs List performance
├── examples/
│   ├── selection_demo.py                     # Selection algorithm demonstrations
│   ├── data_structures_demo.py               # Data structure demonstrations
│   └── generate_plots.py                     # Script to reproduce all plots
├── src/
│   ├── [deterministic_algorithm.py](src/deterministic_algorithm.py)            # Deterministic selection (Median of Medians)
│   ├── [randomized_algorithm.py](src/randomized_algorithm.py)               # Randomized selection (Quickselect)
│   ├── [data_structures.py](src/data_structures.py)                   # Arrays, Stacks, Queues, Linked Lists, Trees
│   └── [benchmark.py](src/benchmark.py)                         # Benchmarking utilities
├── tests/
│   ├── [test_deterministic_algorithm.py](tests/test_deterministic_algorithm.py)      # Tests for deterministic selection
│   ├── [test_randomized_algorithm.py](tests/test_randomized_algorithm.py)         # Tests for randomized selection
│   └── [test_data_structures.py](tests/test_data_structures.py)              # Tests for data structures
├── requirements.txt                          # Python dependencies
├── README.md                                 # Project documentation (this file)
└── REPORT.md                                 # Detailed analysis report
```

## Part 1: Selection Algorithms

### Implementation

#### Deterministic Selection (Median of Medians)
- **File:** [`src/deterministic_algorithm.py`](src/deterministic_algorithm.py)
- **Algorithm:** Median of Medians algorithm for worst-case O(n) selection
- **Key Features:**
  - Groups elements into groups of 5
  - Recursively finds median of medians as pivot
  - Guarantees worst-case linear time complexity
  - Handles edge cases (empty arrays, invalid k values)

#### Randomized Selection (Quickselect)
- **File:** [`src/randomized_algorithm.py`](src/randomized_algorithm.py)
- **Algorithm:** Randomized Quickselect for expected O(n) selection
- **Key Features:**
  - Random pivot selection
  - Expected linear time complexity
  - Optional seed for reproducibility
  - Efficient average-case performance

### API Highlights

**Deterministic Selection:**
```python
deterministic_select(arr, k, key=None)
find_median(arr, key=None)
```

**Randomized Selection:**
```python
randomized_select(arr, k, key=None, seed=None)
find_median(arr, key=None, seed=None)
```

### Theoretical Performance Analysis

| Algorithm | Best Case | Average Case | Worst Case | Space Complexity |
|-----------|-----------|--------------|------------|------------------|
| Deterministic | O(n) | O(n) | O(n) | O(log n) |
| Randomized | O(n) | O(n) | O(n²) | O(log n) |

**Key Insights:**
- **Deterministic:** Uses Median of Medians to guarantee a good pivot, ensuring worst-case O(n) time. The algorithm groups elements into 5, finds medians, then recursively finds the median of medians. This guarantees at least 30% of elements on each side of the pivot.
- **Randomized:** Random pivot selection provides expected O(n) performance. While worst-case is O(n²), the probability of encountering worst-case behavior is exponentially small.
- **Space Complexity:** Both algorithms use O(log n) space for recursion stack in the average case, O(n) in worst case for randomized.

## Part 2: Elementary Data Structures

### Implementation

#### Dynamic Array
- **File:** `src/data_structures.py`
- **Operations:** append, insert, delete, search, access
- **Time Complexity:**
  - Access: O(1)
  - Append: O(1) amortized
  - Insert: O(n)
  - Delete: O(n)
  - Search: O(n)

#### Matrix
- **File:** `src/data_structures.py`
- **Operations:** get, set
- **Time Complexity:** O(1) for all operations

#### Stack
- **File:** `src/data_structures.py`
- **Implementation:** Using Python list (dynamic array)
- **Operations:** push, pop, peek, is_empty, size
- **Time Complexity:**
  - Push: O(1) amortized
  - Pop: O(1)
  - Peek: O(1)

#### Queue
- **File:** `src/data_structures.py`
- **Implementation:** Using Python list (dynamic array)
- **Operations:** enqueue, dequeue, peek, is_empty, size
- **Time Complexity:**
  - Enqueue: O(1) amortized
  - Dequeue: O(n) (can be optimized with circular buffer)
  - Peek: O(1)

#### Linked List
- **File:** `src/data_structures.py`
- **Type:** Singly linked list with head and tail pointers
- **Operations:** append, prepend, insert, delete, search, get
- **Time Complexity:**
  - Append: O(1)
  - Prepend: O(1)
  - Insert: O(n)
  - Delete: O(n)
  - Access: O(n)
  - Search: O(n)

#### Rooted Tree
- **File:** `src/data_structures.py`
- **Implementation:** Using linked nodes with parent-child relationships
- **Operations:** insert, delete, search, traverse (preorder, postorder)
- **Time Complexity:**
  - Insert: O(n) for search + O(1) for insertion
  - Delete: O(n)
  - Search: O(n)
  - Traversal: O(n)

### Trade-offs Analysis

**Arrays vs Linked Lists:**
- **Arrays:** Fast random access (O(1)), cache-friendly, but fixed size or expensive resizing
- **Linked Lists:** Dynamic size, efficient insertion/deletion at ends, but O(n) access and extra memory for pointers

**Stack/Queue Implementation:**
- **Using Arrays:** Simple, cache-friendly, but queue dequeue is O(n)
- **Using Linked Lists:** O(1) for all operations, but more memory overhead

## Getting Started

### Prerequisites

- Python 3.10 or later
- Recommended to use a virtual environment

### Installation

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Running the Examples

```bash
python examples/selection_demo.py          # Selection algorithm demonstrations
python examples/data_structures_demo.py    # Data structure demonstrations
python examples/generate_plots.py          # Regenerate all figures in docs/
```

## Running Tests

```bash
python -m pytest
```

The test suite verifies correctness for:
- Deterministic selection algorithm
- Randomized selection algorithm
- All data structure implementations

## Reproducing the Empirical Study

1. Activate your environment and install dependencies.
2. Run `python examples/generate_plots.py`.
   - Benchmarks may take several minutes depending on hardware.
3. Generated figures will be written to the `docs/` directory.

## Learning Outcomes

Through this assignment, I have achieved the following learning outcomes:

- **Algorithm Implementation**: Successfully implemented both deterministic (Median of Medians) and randomized (Quickselect) selection algorithms from scratch, understanding their theoretical foundations and practical trade-offs.

- **Complexity Analysis**: Gained deep understanding of amortized analysis, probabilistic analysis, and the difference between worst-case, average-case, and expected time complexities.

- **Data Structure Mastery**: Implemented fundamental data structures (dynamic arrays, stacks, queues, linked lists, and trees) from scratch, understanding their operations, trade-offs, and appropriate use cases.

- **Empirical Analysis**: Conducted comprehensive benchmarking across multiple input distributions, learning to interpret performance data and relate empirical results to theoretical predictions.

- **Software Engineering**: Applied best practices including comprehensive testing, error handling, code documentation, and modular design.

## Code Screenshots

Below are screenshots of the actual implementations and testing setup:

![Deterministic Selection Implementation](docs/screenshot_deterministic.png)
*Figure 1: Deterministic selection algorithm implementation showing the Median of Medians function*

![Randomized Selection Implementation](docs/screenshot_randomized.png)
*Figure 2: Randomized selection algorithm implementation with random pivot selection*

![Data Structures Implementation](docs/screenshot_datastructures.png)
*Figure 3: Data structures implementation showing linked list and tree classes*

![Test Execution](docs/screenshot_tests.png)
*Figure 4: Running comprehensive test suite to validate all implementations*

![Benchmark Execution](docs/screenshot_benchmarks.png)
*Figure 5: Benchmark execution showing performance comparison between algorithms*

## Practical Applications

### Selection Algorithms
- **Statistics:** Finding medians, percentiles, and order statistics
- **Database Systems:** Top-k queries, ranking
- **Machine Learning:** Feature selection, outlier detection
- **Operating Systems:** Process scheduling, priority queues

### Data Structures
- **Arrays:** General-purpose storage, matrices for scientific computing
- **Stacks:** Expression evaluation, undo/redo functionality, function call management
- **Queues:** Task scheduling, breadth-first search, message queues
- **Linked Lists:** Dynamic memory allocation, implementing other data structures
- **Trees:** File systems, hierarchical data representation, decision trees

## Academic Integrity Statement

This project is submitted for academic evaluation in MSCS532 – Data Structures and Algorithms. All code, analysis, and documentation were authored by Carlos Gutierrez for the specific purpose of this assignment.