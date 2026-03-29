import pytest
from solution import merge_sorted_arrays


class TestMergeSortedArrays:
    def test_basic_merge(self):
        assert merge_sorted_arrays([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    
    def test_non_overlapping(self):
        assert merge_sorted_arrays([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    
    def test_first_array_empty(self):
        assert merge_sorted_arrays([], [1, 2, 3]) == [1, 2, 3]
    
    def test_second_array_empty(self):
        assert merge_sorted_arrays([1, 2, 3], []) == [1, 2, 3]
    
    def test_both_arrays_empty(self):
        assert merge_sorted_arrays([], []) == []
    
    def test_different_lengths(self):
        assert merge_sorted_arrays([1, 5, 9], [2, 3, 8, 13]) == [1, 2, 3, 5, 8, 9, 13]
    
    def test_negative_numbers(self):
        assert merge_sorted_arrays([-5, -1, 0], [-3, 2, 4]) == [-5, -3, -1, 0, 2, 4]
    
    def test_duplicate_elements(self):
        assert merge_sorted_arrays([1, 2, 2, 3], [2, 3, 4]) == [1, 2, 2, 2, 3, 3, 4]