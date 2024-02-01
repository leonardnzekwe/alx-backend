#!/usr/bin/env python3
""" LRUCache module
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache inherits from BaseCaching
    and implements a caching system using LRU algorithm
    """

    def __init__(self):
        """Initialize LRUCache"""
        super().__init__()
        self.order_used = []

    def put(self, key, item):
        """Add an item in the cache using LRU algorithm"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the least recently used item (LRU)
                lru_key = self.order_used.pop(0)
                del self.cache_data[lru_key]
                print("DISCARD: {}".format(lru_key))
            self.cache_data[key] = item
            self.order_used.append(key)

    def get(self, key):
        """Get an item by key and update order_used"""
        if key is not None and key in self.cache_data:
            # Update order_used to reflect recent use
            self.order_used.remove(key)
            self.order_used.append(key)
            return self.cache_data[key]
        return None
