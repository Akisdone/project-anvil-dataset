import pytest
import solution
def test_1_strong():
    assert solution.check_password_strength("Ab1!cdefghijk") == "Strong"

def test_2_medium_length_only():
    assert solution.check_password_strength("abcdefgh") == "Weak"

def test_3_medium_mixed():
    assert solution.check_password_strength("pass1234") == "Medium"

def test_4_very_short():
    assert solution.check_password_strength("Ab1!") == "Weak"

def test_5_no_special_char():
    assert solution.check_password_strength("Ab12cdefghij") == "Medium"

def test_6_only_special_chars():
    assert solution.check_password_strength("!!!!!!!!") == "Weak"

def test_7_exactly_eight_medium():
    assert solution.check_password_strength("A1bcdefg") == "Medium"

def test_8_all_categories_but_short():
    assert solution.check_password_strength("A1!b2cd") == "Medium"

def test_9_spaces_allowed():
    assert solution.check_password_strength("Password 123!") == "Strong"

def test_10_empty_string():
    assert solution.check_password_strength("") == "Weak"