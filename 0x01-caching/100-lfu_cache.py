#!/usr/bin/env python3
""" LFUCache module
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache inherits from BaseCaching
    and implements a caching system using LFU algorithm
    """

    def __init__(self):
        """Initialize LFUCache"""
        super().__init__()
        self.frequency = {}
        self.order_used = []

    def put(self, key, item):
        """Add an item in the cache using LFU algorithm"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the least frequency used item (LFU)
                min_freq = min(self.frequency.values())
                lfu_keys = [
                    k for k, v in self.frequency.items() if v == min_freq
                ]

                if len(lfu_keys) > 1:
                    # Use LRU to discard the least recently used among LFU keys
                    lru_key = min(
                        lfu_keys, key=lambda k: self.order_used.index(k)
                    )
                else:
                    lru_key = lfu_keys[0]

                del self.cache_data[lru_key]
                del self.frequency[lru_key]
                self.order_used.remove(lru_key)
                print("DISCARD: {}".format(lru_key))

            self.cache_data[key] = item
            self.frequency[key] = self.frequency.get(key, 0) + 1
            self.order_used.append(key)

    def get(self, key):
        """Get an item by key and update frequency and order_used"""
        if key is not None and key in self.cache_data:
            # Update frequency and order_used
            self.frequency[key] += 1
            self.order_used.remove(key)
            self.order_used.append(key)
            return self.cache_data[key]
        return None
