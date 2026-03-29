import pytest
import solution
class TestValidateEmail:
    def test_valid_simple_email(self):
        assert solution.validate_email("user@example.com") == True
    
    def test_valid_with_subdomain(self):
        assert solution.validate_email("user@mail.example.co.uk") == True
    
    def test_valid_with_numbers(self):
        assert solution.validate_email("user123@example.com") == True
    
    def test_valid_single_char_parts(self):
        assert solution.validate_email("a@b.c") == True
    
    def test_invalid_no_at_symbol(self):
        assert solution.validate_email("userexample.com") == False
    
    def test_invalid_multiple_at_symbols(self):
        assert solution.validate_email("user@@example.com") == False
    
    def test_invalid_no_username(self):
        assert solution.validate_email("@example.com") == False
    
    def test_invalid_no_domain(self):
        assert solution.validate_email("user@") == False
    
    def test_invalid_no_dot_in_domain(self):
        assert solution.validate_email("user@example") == False
    
    def test_invalid_space_in_email(self):
        assert solution.validate_email("user @example.com") == False