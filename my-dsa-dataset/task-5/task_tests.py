from solution import is_balanced

def test_1_simple():
    assert is_balanced("()") is True

def test_2_nested():
    assert is_balanced("{[()]}") is True

def test_3_mismatch():
    assert is_balanced("(]") is False

def test_4_interleaved():
    assert is_balanced("([)]") is False

def test_5_unclosed():
    assert is_balanced("(((") is False

def test_6_empty():
    assert is_balanced("") is True