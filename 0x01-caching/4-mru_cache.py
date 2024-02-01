#!/usr/bin/env python3
""" MRUCache module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache inherits from BaseCaching
    and implements a caching system using MRU algorithm
    """

    def __init__(self):
        """Initialize MRUCache"""
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache using MRU algorithm"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the most recently used item (MRU)
                mru_key = next(iter(self.cache_data))
                del self.cache_data[mru_key]
                print("DISCARD: {}".format(mru_key))
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key and update order_used"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
