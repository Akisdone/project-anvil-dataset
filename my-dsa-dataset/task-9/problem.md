# Task: Implement LRU Cache

Implement an LRU (Least Recently Used) Cache class with the following methods:

## Class: `LRUCache`

### Constructor
`__init__(self, capacity: int)` - Initialize cache with a given capacity

### Methods

**`get(key: int) -> int`**
- Returns the value of the key if it exists
- Returns -1 if the key does not exist
- Mark the key as recently used

**`put(key: int, value: int) -> None`**
- Set the value of the key if it exists
- If the key does not exist, insert the key-value pair
- If the cache is at capacity, remove the least recently used key first

## Rules

- Both `get` and `put` operations should run in O(1) time
- Capacity is always positive
- Cache is initially empty

## Example Usage
```
cache = LRUCache(2)
cache.put(1, 1)    # cache: {1: 1}
cache.put(2, 2)    # cache: {1: 1, 2: 2}
cache.get(1)       # returns 1, cache: {2: 2, 1: 1}
cache.put(3, 3)    # capacity full, remove 2, cache: {1: 1, 3: 3}
cache.get(2)       # returns -1 (not found)
cache.put(4, 4)    # capacity full, remove 1, cache: {3: 3, 4: 4}
cache.get(3)       # returns 3
cache.get(4)       # returns 4
```