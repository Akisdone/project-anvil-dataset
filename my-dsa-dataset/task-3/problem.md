# Task: Deep Key Finder

Implement a function `get_deep_value(data: dict, path: str, default=None)` that retrieves a value from a nested dictionary using a dot-separated path string.

### Requirements:
1. The `path` is a string representing keys separated by dots (e.g., `"user.profile.name"`).
2. The function must traverse the dictionary according to the path.
3. If any key in the path does not exist, or if the path is blocked by a non-dictionary object (that isn't a list being indexed), return the `default` value.
4. **List Support:** If a part of the path is a digit (e.g., `"0"`, `"1"`), and the current object is a list, the function should treat that digit as an index.
5. If the `path` is an empty string, return the `default`.

### Examples:
- `data = {"user": {"settings": {"theme": "dark"}}}`
  `get_deep_value(data, "user.settings.theme")` -> `"dark"`

- `data = {"items": ["apple", "banana"]}`
  `get_deep_value(data, "items.1")` -> `"banana"`

- `data = {"a": 1}`
  `get_deep_value(data, "a.b.c", default="Missing")` -> `"Missing"`