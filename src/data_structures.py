"""
Elementary Data Structures Implementation

This module implements basic data structures including arrays, stacks, queues,
linked lists, and rooted trees.

Author: Carlos Gutierrez
Course: MSCS532 - Data Structures and Algorithms
"""

from typing import Optional, Any, List


# ============================================================================
# Arrays and Matrices
# ============================================================================

class DynamicArray:
    """
    A dynamic array implementation with basic operations.
    
    Time Complexity:
        - Access: O(1)
        - Insertion at end: O(1) amortized
        - Insertion at index: O(n)
        - Deletion: O(n)
        - Search: O(n)
    """
    
    def __init__(self, initial_capacity: int = 10):
        """Initialize an empty dynamic array."""
        self._capacity = initial_capacity
        self._size = 0
        self._data = [None] * initial_capacity
    
    def __len__(self) -> int:
        """Return the number of elements in the array."""
        return self._size
    
    def __getitem__(self, index: int) -> Any:
        """Get element at index."""
        if index < 0 or index >= self._size:
            raise IndexError(f"Index {index} out of range")
        return self._data[index]
    
    def __setitem__(self, index: int, value: Any) -> None:
        """Set element at index."""
        if index < 0 or index >= self._size:
            raise IndexError(f"Index {index} out of range")
        self._data[index] = value
    
    def append(self, value: Any) -> None:
        """Append element to the end of the array. O(1) amortized."""
        if self._size >= self._capacity:
            self._resize()
        self._data[self._size] = value
        self._size += 1
    
    def insert(self, index: int, value: Any) -> None:
        """Insert element at index. O(n)."""
        if index < 0 or index > self._size:
            raise IndexError(f"Index {index} out of range")
        
        if self._size >= self._capacity:
            self._resize()
        
        # Shift elements to the right
        for i in range(self._size, index, -1):
            self._data[i] = self._data[i - 1]
        
        self._data[index] = value
        self._size += 1
    
    def delete(self, index: int) -> Any:
        """Delete element at index and return it. O(n)."""
        if index < 0 or index >= self._size:
            raise IndexError(f"Index {index} out of range")
        
        value = self._data[index]
        
        # Shift elements to the left
        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]
        
        self._size -= 1
        return value
    
    def search(self, value: Any) -> int:
        """Search for value and return its index, or -1 if not found. O(n)."""
        for i in range(self._size):
            if self._data[i] == value:
                return i
        return -1
    
    def _resize(self) -> None:
        """Double the capacity of the array."""
        self._capacity *= 2
        new_data = [None] * self._capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
    
    def __str__(self) -> str:
        """String representation of the array."""
        return str([self._data[i] for i in range(self._size)])


class Matrix:
    """
    A 2D matrix implementation with basic operations.
    
    Time Complexity:
        - Access: O(1)
        - Insertion: O(1)
        - Deletion: O(1)
        - Matrix operations: O(n*m) where n, m are dimensions
    """
    
    def __init__(self, rows: int, cols: int, initial_value: Any = 0):
        """Initialize a matrix with given dimensions."""
        self.rows = rows
        self.cols = cols
        self._data = [[initial_value for _ in range(cols)] for _ in range(rows)]
    
    def __getitem__(self, key: tuple) -> Any:
        """Get element at (row, col)."""
        row, col = key
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise IndexError(f"Index ({row}, {col}) out of range")
        return self._data[row][col]
    
    def __setitem__(self, key: tuple, value: Any) -> None:
        """Set element at (row, col)."""
        row, col = key
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise IndexError(f"Index ({row}, {col}) out of range")
        self._data[row][col] = value
    
    def __str__(self) -> str:
        """String representation of the matrix."""
        return '\n'.join([' '.join(map(str, row)) for row in self._data])


# ============================================================================
# Stacks and Queues
# ============================================================================

class Stack:
    """
    Stack implementation using a dynamic array.
    
    Time Complexity:
        - Push: O(1) amortized
        - Pop: O(1)
        - Peek: O(1)
        - Search: O(n)
    """
    
    def __init__(self):
        """Initialize an empty stack."""
        self._data = []
    
    def push(self, value: Any) -> None:
        """Push element onto the stack. O(1) amortized."""
        self._data.append(value)
    
    def pop(self) -> Any:
        """Pop and return the top element. O(1)."""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._data.pop()
    
    def peek(self) -> Any:
        """Return the top element without removing it. O(1)."""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._data[-1]
    
    def is_empty(self) -> bool:
        """Check if the stack is empty. O(1)."""
        return len(self._data) == 0
    
    def size(self) -> int:
        """Return the number of elements in the stack. O(1)."""
        return len(self._data)
    
    def __str__(self) -> str:
        """String representation of the stack."""
        return str(self._data)


class Queue:
    """
    Queue implementation using a dynamic array.
    
    Time Complexity:
        - Enqueue: O(1) amortized
        - Dequeue: O(n) (can be optimized to O(1) with circular buffer)
        - Peek: O(1)
        - Search: O(n)
    """
    
    def __init__(self):
        """Initialize an empty queue."""
        self._data = []
    
    def enqueue(self, value: Any) -> None:
        """Add element to the rear of the queue. O(1) amortized."""
        self._data.append(value)
    
    def dequeue(self) -> Any:
        """Remove and return the front element. O(n)."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._data.pop(0)
    
    def peek(self) -> Any:
        """Return the front element without removing it. O(1)."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._data[0]
    
    def is_empty(self) -> bool:
        """Check if the queue is empty. O(1)."""
        return len(self._data) == 0
    
    def size(self) -> int:
        """Return the number of elements in the queue. O(1)."""
        return len(self._data)
    
    def __str__(self) -> str:
        """String representation of the queue."""
        return str(self._data)


# ============================================================================
# Linked Lists
# ============================================================================

class ListNode:
    """Node for linked list."""
    
    def __init__(self, value: Any):
        self.value = value
        self.next: Optional['ListNode'] = None


class LinkedList:
    """
    Singly linked list implementation.
    
    Time Complexity:
        - Access: O(n)
        - Insertion at head: O(1)
        - Insertion at tail: O(1) with tail pointer
        - Insertion at index: O(n)
        - Deletion: O(n)
        - Search: O(n)
    """
    
    def __init__(self):
        """Initialize an empty linked list."""
        self.head: Optional[ListNode] = None
        self.tail: Optional[ListNode] = None
        self._size = 0
    
    def __len__(self) -> int:
        """Return the number of elements in the list."""
        return self._size
    
    def append(self, value: Any) -> None:
        """Append element to the end of the list. O(1)."""
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1
    
    def prepend(self, value: Any) -> None:
        """Prepend element to the beginning of the list. O(1)."""
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self._size += 1
    
    def insert(self, index: int, value: Any) -> None:
        """Insert element at index. O(n)."""
        if index < 0 or index > self._size:
            raise IndexError(f"Index {index} out of range")
        
        if index == 0:
            self.prepend(value)
            return
        
        if index == self._size:
            self.append(value)
            return
        
        new_node = ListNode(value)
        current = self.head
        for _ in range(index - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        self._size += 1
    
    def delete(self, index: int) -> Any:
        """Delete element at index and return it. O(n)."""
        if index < 0 or index >= self._size:
            raise IndexError(f"Index {index} out of range")
        
        if index == 0:
            value = self.head.value
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return value
        
        current = self.head
        for _ in range(index - 1):
            current = current.next
        
        value = current.next.value
        current.next = current.next.next
        
        if current.next is None:
            self.tail = current
        
        self._size -= 1
        return value
    
    def search(self, value: Any) -> int:
        """Search for value and return its index, or -1 if not found. O(n)."""
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1
    
    def get(self, index: int) -> Any:
        """Get element at index. O(n)."""
        if index < 0 or index >= self._size:
            raise IndexError(f"Index {index} out of range")
        
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value
    
    def __str__(self) -> str:
        """String representation of the linked list."""
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return ' -> '.join(values) if values else 'Empty'


# ============================================================================
# Rooted Trees
# ============================================================================

class TreeNode:
    """Node for a rooted tree."""
    
    def __init__(self, value: Any):
        self.value = value
        self.children: List['TreeNode'] = []
        self.parent: Optional['TreeNode'] = None
    
    def add_child(self, child: 'TreeNode') -> None:
        """Add a child node."""
        child.parent = self
        self.children.append(child)
    
    def remove_child(self, child: 'TreeNode') -> None:
        """Remove a child node."""
        if child in self.children:
            child.parent = None
            self.children.remove(child)


class Tree:
    """
    Rooted tree implementation using linked nodes.
    
    Time Complexity:
        - Insertion: O(1)
        - Deletion: O(n) worst case
        - Search: O(n)
        - Traversal: O(n)
    """
    
    def __init__(self, root_value: Any = None):
        """Initialize a tree with an optional root."""
        self.root: Optional[TreeNode] = TreeNode(root_value) if root_value is not None else None
    
    def insert(self, parent_value: Any, value: Any) -> bool:
        """
        Insert a new node as a child of the node with parent_value.
        Returns True if successful, False if parent not found.
        O(n) for search, O(1) for insertion.
        """
        if self.root is None:
            self.root = TreeNode(value)
            return True
        
        parent = self._find_node(self.root, parent_value)
        if parent is None:
            return False
        
        new_node = TreeNode(value)
        parent.add_child(new_node)
        return True
    
    def delete(self, value: Any) -> bool:
        """
        Delete a node with the given value.
        Returns True if successful, False if node not found.
        O(n).
        """
        if self.root is None:
            return False
        
        if self.root.value == value:
            # If root has children, make first child the new root
            if self.root.children:
                new_root = self.root.children[0]
                new_root.parent = None
                # Add remaining children to new root
                for child in self.root.children[1:]:
                    new_root.add_child(child)
                self.root = new_root
            else:
                self.root = None
            return True
        
        node = self._find_node(self.root, value)
        if node is None:
            return False
        
        # Save parent and children before removing from parent
        parent = node.parent
        children_to_move = list(node.children)
        
        if parent:
            parent.remove_child(node)
            # Add children to parent
            for child in children_to_move:
                parent.add_child(child)
        else:
            # Node has no parent (shouldn't happen if not root, but handle it)
            if children_to_move:
                # Make first child the new root
                self.root = children_to_move[0]
                self.root.parent = None
                # Add remaining children
                for child in children_to_move[1:]:
                    self.root.add_child(child)
            else:
                self.root = None
        
        return True
    
    def search(self, value: Any) -> bool:
        """Search for a value in the tree. O(n)."""
        if self.root is None:
            return False
        return self._find_node(self.root, value) is not None
    
    def _find_node(self, node: TreeNode, value: Any) -> Optional[TreeNode]:
        """Helper method to find a node with given value. O(n)."""
        if node.value == value:
            return node
        
        for child in node.children:
            result = self._find_node(child, value)
            if result:
                return result
        
        return None
    
    def traverse_preorder(self) -> List[Any]:
        """Traverse tree in preorder (root, children). O(n)."""
        result = []
        if self.root:
            self._preorder_helper(self.root, result)
        return result
    
    def _preorder_helper(self, node: TreeNode, result: List[Any]) -> None:
        """Helper for preorder traversal."""
        result.append(node.value)
        for child in node.children:
            self._preorder_helper(child, result)
    
    def traverse_postorder(self) -> List[Any]:
        """Traverse tree in postorder (children, root). O(n)."""
        result = []
        if self.root:
            self._postorder_helper(self.root, result)
        return result
    
    def _postorder_helper(self, node: TreeNode, result: List[Any]) -> None:
        """Helper for postorder traversal."""
        for child in node.children:
            self._postorder_helper(child, result)
        result.append(node.value)
    
    def height(self) -> int:
        """Calculate the height of the tree. O(n)."""
        if self.root is None:
            return -1
        return self._height_helper(self.root)
    
    def _height_helper(self, node: TreeNode) -> int:
        """Helper to calculate height."""
        if not node.children:
            return 0
        return 1 + max(self._height_helper(child) for child in node.children)

