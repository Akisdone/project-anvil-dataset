import solution
def test_1_basic_nesting():
    data = {"user": {"id": 101}}
    assert solution.get_deep_value(data, "user.id") == 101

def test_2_missing_key():
    data = {"user": {"id": 101}}
    assert solution.get_deep_value(data, "user.name", "Unknown") == "Unknown"

def test_3_list_access():
    data = {"tags": ["python", "coding"]}
    assert solution.get_deep_value(data, "tags.1") == "coding"

def test_4_deep_list_nesting():
    data = {"users": [{"name": "Alice"}, {"name": "Bob"}]}
    assert solution.get_deep_value(data, "users.1.name") == "Bob"

def test_5_invalid_type_access():
    data = {"count": 10}
    assert solution.get_deep_value(data, "count.item") is None

def test_6_empty_string_path():
    assert solution.get_deep_value({"a": 1}, "") is None
    
def test_7_none_data():
    """Test 7: Handle when the data itself is None"""
    assert solution.get_deep_value(None, "any.path", default="Error") == "Error"

def test_8_deep_nesting_10_levels():
    """Test 8: Handle very deep nesting"""
    data = {"1": {"2": {"3": {"4": {"5": {"6": {"7": {"8": {"9": {"10": "winner"}}}}}}}}}}
    path = "1.2.3.4.5.6.7.8.9.10"
    assert solution.get_deep_value(data, path) == "winner"

def test_9_special_characters_in_keys():
    """Test 9: Keys with spaces or symbols (not dots)"""
    data = {"my key!": {"@user": "found_me"}}
    assert solution.get_deep_value(data, "my key!.@user") == "found_me"

def test_10_index_out_of_range():
    """Test 10: Handle list index that doesn't exist"""
    data = {"items": ["apple"]}
    assert solution.get_deep_value(data, "items.5", default="Missing") == "Missing"