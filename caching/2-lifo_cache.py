#!/usr/bin/python3
""" LIFOcache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache defines:
      - Inherits from BaseCaching
      - Caching system
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key not in self.cache_data:
                    discarded_key = self.keys.pop()
                    del self.cache_data[discarded_key]
                    print("DISCARD:", discarded_key)
            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
