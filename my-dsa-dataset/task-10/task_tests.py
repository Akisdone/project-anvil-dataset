import pytest
from solution import find_rotation_point


class TestFindRotationPoint:
    def test_typical_rotation(self):
        assert find_rotation_point([4, 5, 6, 7, 1, 2, 3]) == 4
    
    def test_no_rotation(self):
        assert find_rotation_point([1, 2, 3, 4, 5, 6, 7]) == 0
    
    def test_rotation_mid_point(self):
        assert find_rotation_point([3, 4, 5, 1, 2]) == 3
    
    def test_rotation_early(self):
        assert find_rotation_point([5, 1, 2, 3, 4]) == 1
    
    def test_single_element(self):
        assert find_rotation_point([1]) == 0
    
    def test_two_elements_rotated(self):
        assert find_rotation_point([2, 1]) == 1
    
    def test_two_elements_not_rotated(self):
        assert find_rotation_point([1, 2]) == 0
    
    def test_rotation_near_end(self):
        assert find_rotation_point([6, 7, 1, 2, 3, 4, 5]) == 2
    
    def test_large_array_rotated(self):
        assert find_rotation_point([50, 60, 70, 80, 90, 10, 20, 30, 40]) == 5
    
    def test_rotation_at_position_one(self):
        assert find_rotation_point([7, 1, 2, 3, 4, 5, 6]) == 1