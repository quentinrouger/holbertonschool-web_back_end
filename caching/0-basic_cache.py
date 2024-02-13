#!/usr/bin/python3
""" BasicCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache defines:
      - Inherits from BaseCaching
      - Caching system
    """

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                keys = list(self.cache_data.keys())
                del self.cache_data[keys[0]]
            else:
                return None

    def get(self, key):
        """ Get an item by key
        """
        if key and key in self.cache_data:
            return self.cache_data.get(key)
        else:
            return None
