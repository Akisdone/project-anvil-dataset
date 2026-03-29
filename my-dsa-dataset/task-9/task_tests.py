import pytest
import solution
class TestLRUCache:
    def test_basic_get_put(self):
        cache = solution.LRUCache(2)
        cache.put(1, 1)
        assert cache.get(1) == 1
    
    def test_cache_miss(self):
        cache = solution.LRUCache(2)
        cache.put(1, 1)
        assert cache.get(2) == -1
    
    def test_capacity_eviction(self):
        cache = solution.LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(3, 3)
        assert cache.get(1) == -1
        assert cache.get(2) == 2
        assert cache.get(3) == 3
    
    def test_get_updates_recently_used(self):
        cache = solution.LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.get(1)
        cache.put(3, 3)
        assert cache.get(1) == 1
        assert cache.get(2) == -1
    
    def test_update_existing_key(self):
        cache = solution.LRUCache(2)
        cache.put(1, 1)
        cache.put(1, 2)
        assert cache.get(1) == 2
    
    def test_capacity_one(self):
        cache = solution.LRUCache(1)
        cache.put(1, 1)
        cache.put(2, 2)
        assert cache.get(1) == -1
        assert cache.get(2) == 2
    
    def test_multiple_operations(self):
        cache = solution.LRUCache(3)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(3, 3)
        assert cache.get(1) == 1
        cache.put(4, 4)
        assert cache.get(2) == -1
        assert cache.get(3) == 3
        assert cache.get(4) == 4
    
    def test_lru_order(self):
        cache = solution.LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.get(1)
        cache.put(3, 3)
        assert cache.get(2) == -1
        assert cache.get(1) == 1
        assert cache.get(3) == 3