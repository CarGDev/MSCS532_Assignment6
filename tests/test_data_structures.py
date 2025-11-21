"""
Unit tests for elementary data structures.

Author: Carlos Gutierrez
Course: MSCS532 - Data Structures and Algorithms
"""

import pytest
from src.data_structures import (
    DynamicArray, Matrix, Stack, Queue, LinkedList, Tree, TreeNode
)


class TestDynamicArray:
    """Test cases for DynamicArray."""
    
    def test_initialization(self):
        """Test array initialization."""
        arr = DynamicArray()
        assert len(arr) == 0
    
    def test_append(self):
        """Test append operation."""
        arr = DynamicArray()
        arr.append(1)
        arr.append(2)
        assert len(arr) == 2
        assert arr[0] == 1
        assert arr[1] == 2
    
    def test_insert(self):
        """Test insert operation."""
        arr = DynamicArray()
        arr.append(1)
        arr.append(3)
        arr.insert(1, 2)
        assert arr[1] == 2
        assert len(arr) == 3
    
    def test_delete(self):
        """Test delete operation."""
        arr = DynamicArray()
        arr.append(1)
        arr.append(2)
        arr.append(3)
        value = arr.delete(1)
        assert value == 2
        assert len(arr) == 2
        assert arr[1] == 3
    
    def test_search(self):
        """Test search operation."""
        arr = DynamicArray()
        arr.append(1)
        arr.append(2)
        arr.append(3)
        assert arr.search(2) == 1
        assert arr.search(4) == -1
    
    def test_index_error(self):
        """Test index error handling."""
        arr = DynamicArray()
        with pytest.raises(IndexError):
            _ = arr[0]
        arr.append(1)
        with pytest.raises(IndexError):
            _ = arr[1]


class TestMatrix:
    """Test cases for Matrix."""
    
    def test_initialization(self):
        """Test matrix initialization."""
        matrix = Matrix(3, 4)
        assert matrix.rows == 3
        assert matrix.cols == 4
    
    def test_get_set(self):
        """Test get and set operations."""
        matrix = Matrix(2, 2)
        matrix[0, 0] = 1
        matrix[0, 1] = 2
        matrix[1, 0] = 3
        matrix[1, 1] = 4
        assert matrix[0, 0] == 1
        assert matrix[1, 1] == 4
    
    def test_index_error(self):
        """Test index error handling."""
        matrix = Matrix(2, 2)
        with pytest.raises(IndexError):
            _ = matrix[3, 0]


class TestStack:
    """Test cases for Stack."""
    
    def test_push_pop(self):
        """Test push and pop operations."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        assert stack.pop() == 2
        assert stack.pop() == 1
    
    def test_peek(self):
        """Test peek operation."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        assert stack.peek() == 2
        assert stack.size() == 2
    
    def test_is_empty(self):
        """Test is_empty operation."""
        stack = Stack()
        assert stack.is_empty()
        stack.push(1)
        assert not stack.is_empty()
    
    def test_empty_pop(self):
        """Test pop from empty stack."""
        stack = Stack()
        with pytest.raises(IndexError):
            stack.pop()


class TestQueue:
    """Test cases for Queue."""
    
    def test_enqueue_dequeue(self):
        """Test enqueue and dequeue operations."""
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        assert queue.dequeue() == 1
        assert queue.dequeue() == 2
    
    def test_peek(self):
        """Test peek operation."""
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        assert queue.peek() == 1
        assert queue.size() == 2
    
    def test_is_empty(self):
        """Test is_empty operation."""
        queue = Queue()
        assert queue.is_empty()
        queue.enqueue(1)
        assert not queue.is_empty()
    
    def test_empty_dequeue(self):
        """Test dequeue from empty queue."""
        queue = Queue()
        with pytest.raises(IndexError):
            queue.dequeue()


class TestLinkedList:
    """Test cases for LinkedList."""
    
    def test_append(self):
        """Test append operation."""
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        assert len(ll) == 2
        assert ll.get(0) == 1
        assert ll.get(1) == 2
    
    def test_prepend(self):
        """Test prepend operation."""
        ll = LinkedList()
        ll.prepend(1)
        ll.prepend(2)
        assert ll.get(0) == 2
        assert ll.get(1) == 1
    
    def test_insert(self):
        """Test insert operation."""
        ll = LinkedList()
        ll.append(1)
        ll.append(3)
        ll.insert(1, 2)
        assert ll.get(1) == 2
        assert len(ll) == 3
    
    def test_delete(self):
        """Test delete operation."""
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        value = ll.delete(1)
        assert value == 2
        assert len(ll) == 2
        assert ll.get(1) == 3
    
    def test_search(self):
        """Test search operation."""
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        assert ll.search(2) == 1
        assert ll.search(4) == -1
    
    def test_index_error(self):
        """Test index error handling."""
        ll = LinkedList()
        with pytest.raises(IndexError):
            ll.get(0)
        ll.append(1)
        with pytest.raises(IndexError):
            ll.get(1)


class TestTree:
    """Test cases for Tree."""
    
    def test_initialization(self):
        """Test tree initialization."""
        tree = Tree(1)
        assert tree.root is not None
        assert tree.root.value == 1
    
    def test_insert(self):
        """Test insert operation."""
        tree = Tree(1)
        assert tree.insert(1, 2)
        assert tree.insert(1, 3)
        assert len(tree.root.children) == 2
    
    def test_search(self):
        """Test search operation."""
        tree = Tree(1)
        tree.insert(1, 2)
        tree.insert(2, 3)
        assert tree.search(1)
        assert tree.search(2)
        assert tree.search(3)
        assert not tree.search(4)
    
    def test_delete(self):
        """Test delete operation."""
        tree = Tree(1)
        tree.insert(1, 2)
        tree.insert(1, 3)
        assert tree.delete(2)
        assert not tree.search(2)
        assert tree.search(3)
    
    def test_traversal(self):
        """Test tree traversal."""
        tree = Tree(1)
        tree.insert(1, 2)
        tree.insert(1, 3)
        tree.insert(2, 4)
        
        preorder = tree.traverse_preorder()
        assert preorder == [1, 2, 4, 3]
        
        postorder = tree.traverse_postorder()
        assert postorder == [4, 2, 3, 1]
    
    def test_height(self):
        """Test height calculation."""
        tree = Tree(1)
        assert tree.height() == 0
        tree.insert(1, 2)
        assert tree.height() == 1
        tree.insert(2, 3)
        assert tree.height() == 2

