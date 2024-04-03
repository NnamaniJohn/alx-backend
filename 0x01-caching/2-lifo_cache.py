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
            first_key = ''
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_key = next(reversed(self.cache_data))
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                self.cache_data.pop(first_key)
                print("DISCARD: {}".format(first_key))

    def get(self, key):
        """
        get
        :param key:
        :return:
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
