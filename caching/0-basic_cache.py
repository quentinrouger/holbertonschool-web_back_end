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
        """ Add an item to the cache """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key)


if __name__ == "__main__":
    my_cache = BasicCache()
