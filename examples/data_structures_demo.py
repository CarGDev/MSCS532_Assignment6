"""
Demonstration of elementary data structures.

This script demonstrates the usage of arrays, stacks, queues, linked lists,
and trees.

Author: Carlos Gutierrez
Course: MSCS532 - Data Structures and Algorithms
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.data_structures import (
    DynamicArray, Matrix, Stack, Queue, LinkedList, Tree
)


def demo_dynamic_array():
    """Demonstrate DynamicArray operations."""
    print("=" * 60)
    print("Dynamic Array Demo")
    print("=" * 60)
    
    arr = DynamicArray()
    
    # Append elements
    print("Appending elements: 1, 2, 3, 4, 5")
    for i in range(1, 6):
        arr.append(i)
    print(f"Array: {arr}")
    print(f"Length: {len(arr)}")
    print()
    
    # Insert element
    print("Inserting 10 at index 2")
    arr.insert(2, 10)
    print(f"Array: {arr}")
    print()
    
    # Delete element
    print("Deleting element at index 3")
    value = arr.delete(3)
    print(f"Deleted value: {value}")
    print(f"Array: {arr}")
    print()
    
    # Search
    print(f"Searching for 10: index {arr.search(10)}")
    print(f"Searching for 99: index {arr.search(99)}")
    print()


def demo_matrix():
    """Demonstrate Matrix operations."""
    print("=" * 60)
    print("Matrix Demo")
    print("=" * 60)
    
    matrix = Matrix(3, 4)
    
    # Fill matrix
    value = 1
    for i in range(3):
        for j in range(4):
            matrix[i, j] = value
            value += 1
    
    print("3x4 Matrix:")
    print(matrix)
    print()
    
    print(f"Element at (1, 2): {matrix[1, 2]}")
    print()


def demo_stack():
    """Demonstrate Stack operations."""
    print("=" * 60)
    print("Stack Demo")
    print("=" * 60)
    
    stack = Stack()
    
    # Push elements
    print("Pushing elements: 1, 2, 3, 4, 5")
    for i in range(1, 6):
        stack.push(i)
    print(f"Stack: {stack}")
    print(f"Size: {stack.size()}")
    print()
    
    # Peek
    print(f"Top element (peek): {stack.peek()}")
    print()
    
    # Pop elements
    print("Popping elements:")
    while not stack.is_empty():
        print(f"  Popped: {stack.pop()}")
    print()


def demo_queue():
    """Demonstrate Queue operations."""
    print("=" * 60)
    print("Queue Demo")
    print("=" * 60)
    
    queue = Queue()
    
    # Enqueue elements
    print("Enqueuing elements: 1, 2, 3, 4, 5")
    for i in range(1, 6):
        queue.enqueue(i)
    print(f"Queue: {queue}")
    print(f"Size: {queue.size()}")
    print()
    
    # Peek
    print(f"Front element (peek): {queue.peek()}")
    print()
    
    # Dequeue elements
    print("Dequeuing elements:")
    while not queue.is_empty():
        print(f"  Dequeued: {queue.dequeue()}")
    print()


def demo_linked_list():
    """Demonstrate LinkedList operations."""
    print("=" * 60)
    print("Linked List Demo")
    print("=" * 60)
    
    ll = LinkedList()
    
    # Append elements
    print("Appending elements: 1, 2, 3, 4, 5")
    for i in range(1, 6):
        ll.append(i)
    print(f"Linked List: {ll}")
    print(f"Length: {len(ll)}")
    print()
    
    # Prepend element
    print("Prepending 0")
    ll.prepend(0)
    print(f"Linked List: {ll}")
    print()
    
    # Insert element
    print("Inserting 10 at index 3")
    ll.insert(3, 10)
    print(f"Linked List: {ll}")
    print()
    
    # Get element
    print(f"Element at index 2: {ll.get(2)}")
    print()
    
    # Search
    print(f"Searching for 10: index {ll.search(10)}")
    print(f"Searching for 99: index {ll.search(99)}")
    print()
    
    # Delete element
    print("Deleting element at index 3")
    value = ll.delete(3)
    print(f"Deleted value: {value}")
    print(f"Linked List: {ll}")
    print()


def demo_tree():
    """Demonstrate Tree operations."""
    print("=" * 60)
    print("Tree Demo")
    print("=" * 60)
    
    tree = Tree(1)
    
    # Build tree
    print("Building tree:")
    print("  1")
    print("  ├── 2")
    print("  │   ├── 4")
    print("  │   └── 5")
    print("  └── 3")
    print("      └── 6")
    
    tree.insert(1, 2)
    tree.insert(1, 3)
    tree.insert(2, 4)
    tree.insert(2, 5)
    tree.insert(3, 6)
    print()
    
    # Search
    print("Searching for values:")
    for value in [1, 2, 3, 4, 5, 6, 7]:
        found = tree.search(value)
        print(f"  {value}: {'Found' if found else 'Not found'}")
    print()
    
    # Traversal
    print("Preorder traversal:", tree.traverse_preorder())
    print("Postorder traversal:", tree.traverse_postorder())
    print()
    
    # Height
    print(f"Tree height: {tree.height()}")
    print()
    
    # Delete
    print("Deleting node 2")
    tree.delete(2)
    print("Preorder traversal after deletion:", tree.traverse_preorder())
    print()


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("Elementary Data Structures Demonstration")
    print("=" * 60 + "\n")
    
    demo_dynamic_array()
    demo_matrix()
    demo_stack()
    demo_queue()
    demo_linked_list()
    demo_tree()
    
    print("=" * 60)
    print("Demo Complete!")
    print("=" * 60)

