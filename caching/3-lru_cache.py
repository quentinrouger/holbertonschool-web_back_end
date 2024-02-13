#!/usr/bin/env python3
""" LRU Cache module
"""
from collections import OrderedDict

BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """ LRUcache defines:
      - Inherits from BaseCaching
      - Caching system
    """
    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
#         """
        if key and item:
            if key not in self.cache_data and\
                    len(self.cache_data) == self.MAX_ITEMS:
                last_item_used = self.cache_data.popitem(last=False)
                print(f"DISCARD: {last_item_used[0]}")
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key and key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data.get(key)
        return None
