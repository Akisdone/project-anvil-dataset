import pytest
import solution
class TestTwoSum:
    def test_basic_two_sum(self):
        assert solution.two_sum([2, 7, 11, 15], 9) == [0, 1]
    
    def test_different_positions(self):
        assert solution.two_sum([3, 2, 4], 6) == [1, 2]
    
    def test_duplicate_elements(self):
        assert solution.two_sum([3, 3], 6) == [0, 1]
    
    def test_no_solution(self):
        assert solution.two_sum([1, 2, 3], 7) == []
    
    def test_empty_array(self):
        assert solution.two_sum([], 5) == []
    
    def test_single_element(self):
        assert solution.two_sum([5], 10) == []
    
    def test_negative_numbers(self):
        assert solution.two_sum([-1, -2, -3, 5, 10], 7) == [2, 4]
    
    def test_zero_target(self):
        assert solution.two_sum([-5, 0, 5, 10], 0) == [0, 2]