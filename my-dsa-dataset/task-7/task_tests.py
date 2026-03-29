import pytest
from solution import is_valid
class TestValidParentheses:
    def test_empty_string(self):
        assert is_valid("") == True
    def test_single_pair(self):
        assert is_valid("()") == True
    def test_multiple_pairs(self):
        assert is_valid("()[]{}") == True
    
    def test_nested_brackets(self):
        assert is_valid("{[()]}") == True
    
    def test_unmatched_opening(self):
        assert is_valid("(") == False
    
    def test_unmatched_closing(self):
        assert is_valid(")") == False
    
    def test_wrong_closing_bracket(self):
        assert is_valid("(]") == False
    
    def test_interleaved_brackets(self):
        assert is_valid("([)]") == False
    
    def test_mismatched_type(self):
        assert is_valid("{[}]") == False
    
    def test_complex_valid(self):
        assert is_valid("([{}])") == True