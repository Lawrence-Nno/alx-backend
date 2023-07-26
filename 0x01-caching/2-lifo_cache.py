#!/usr/bin/python3
"""Create a class LIFOCache that inherits from
   BaseCaching and is a caching system"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """List In First Out Caching System"""
    def __init__(self):
        self.last_put = ""
        super().__init__()

    def put(self, key, item):
        """This func adds an item to the cache"""
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self.cache_data.pop(self.last_put)
            print('DISCARD:', self.last_put)
        if key:
            self.last_put = key

    def get(self, key):
        """This func gets an item from cache by key"""
        if key and key in self.cache_data:
            return self.cache_data.get(key)
        else:
            return None
