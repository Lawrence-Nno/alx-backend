#!/usr/bin/python3
"""Create a class FIFOCache that inherits from
   BaseCaching and is a caching system"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """First In First out caching system"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """This func will add an Item"""
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            to_pop = sorted(self.cache_data)[0]
            self.cache_data.pop(to_pop)
            print('DISCARD:', to_pop)

    def get(self, key):
        """This func obtains an Item"""
        if key and key in self.cache_data:
            return self.cache_data.get(key)
        else:
            return None
