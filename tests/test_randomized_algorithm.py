"""
Unit tests for randomized selection algorithm.

Author: Carlos Gutierrez
Course: MSCS532 - Data Structures and Algorithms
"""

import pytest
from src.randomized_algorithm import randomized_select, find_median


class TestRandomizedSelect:
    """Test cases for randomized_select function."""
    
    def test_basic_selection(self):
        """Test basic selection operations."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        assert randomized_select(arr, 1, seed=42) == 1
        assert randomized_select(arr, 2, seed=42) == 1
        assert randomized_select(arr, 3, seed=42) == 2
        assert randomized_select(arr, 4, seed=42) == 3
        assert randomized_select(arr, len(arr), seed=42) == 9
    
    def test_sorted_array(self):
        """Test on sorted array."""
        arr = list(range(1, 11))
        for i in range(1, 11):
            assert randomized_select(arr, i, seed=42) == i
    
    def test_reverse_sorted_array(self):
        """Test on reverse-sorted array."""
        arr = list(range(10, 0, -1))
        for i in range(1, 11):
            assert randomized_select(arr, i, seed=42) == i
    
    def test_duplicate_elements(self):
        """Test with duplicate elements."""
        arr = [5, 5, 5, 3, 3, 1, 1, 1]
        assert randomized_select(arr, 1, seed=42) == 1
        assert randomized_select(arr, 2, seed=42) == 1
        assert randomized_select(arr, 3, seed=42) == 1
        assert randomized_select(arr, 4, seed=42) == 3
        assert randomized_select(arr, 5, seed=42) == 3
        assert randomized_select(arr, 6, seed=42) == 5
    
    def test_single_element(self):
        """Test with single element."""
        arr = [42]
        assert randomized_select(arr, 1, seed=42) == 42
    
    def test_empty_array(self):
        """Test with empty array."""
        with pytest.raises(IndexError):
            randomized_select([], 1)
    
    def test_invalid_k(self):
        """Test with invalid k values."""
        arr = [1, 2, 3]
        with pytest.raises(ValueError):
            randomized_select(arr, 0)
        with pytest.raises(ValueError):
            randomized_select(arr, 4)
    
    def test_key_function(self):
        """Test with custom key function."""
        arr = [{'value': 3}, {'value': 1}, {'value': 2}]
        result = randomized_select(arr, 2, key=lambda x: x['value'], seed=42)
        assert result['value'] == 2
    
    def test_large_array(self):
        """Test with larger array."""
        arr = list(range(100, 0, -1))
        assert randomized_select(arr, 50, seed=42) == 50
        assert randomized_select(arr, 1, seed=42) == 1
        assert randomized_select(arr, 100, seed=42) == 100
    
    def test_reproducibility(self):
        """Test that results are reproducible with same seed."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        result1 = randomized_select(arr, 4, seed=42)
        result2 = randomized_select(arr, 4, seed=42)
        assert result1 == result2


class TestFindMedian:
    """Test cases for find_median function."""
    
    def test_odd_length(self):
        """Test median of odd-length array."""
        arr = [3, 1, 4, 1, 5]
        assert find_median(arr, seed=42) == 3
    
    def test_even_length(self):
        """Test median of even-length array (returns lower median)."""
        arr = [3, 1, 4, 1, 5, 9]
        assert find_median(arr, seed=42) == 3
    
    def test_sorted_array(self):
        """Test median of sorted array."""
        arr = list(range(1, 11))
        assert find_median(arr, seed=42) == 5
    
    def test_empty_array(self):
        """Test median of empty array."""
        with pytest.raises(ValueError):
            find_median([])

