#!/usr/bin/python3
""" Lifo Caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    FIFOCache
    """

    def __init__(self):
        """
        init
        """
        super().__init__()

    def put(self, key, item):
        """
        put
        :param key:
        :param item:
        :return:
        """
        if key is not None and item is not None:
            if key in self.cache_data.keys():
                self.cache_data.pop(key)
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_key = self.cache_data.popitem()
                print("DISCARD: {}".format(first_key[0]))
            self.cache_data[key] = item

    def get(self, key):
        """
        get
        :param key:
        :return:
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
