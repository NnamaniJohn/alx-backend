#!/usr/bin/python3
""" MRU Caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache
    """

    def __init__(self):
        """
        init
        """
        super().__init__()
        self.freq = {}

    def put(self, key, item):
        """
        put
        :param key:
        :param item:
        :return:
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.freq.keys():
                self.freq[key] = 0
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                if not self.freq:
                    first_key = next(iter(self.cache_data))
                else:
                    first_key = max(self.freq, key=self.freq.get)
                self.cache_data.pop(first_key)
                self.freq.pop(first_key)
                print("DISCARD: {}".format(first_key))

    def get(self, key):
        """
        get
        :param key:
        :return:
        """
        if key is None or key not in self.cache_data.keys():
            return None
        if key not in self.freq.keys():
            self.freq[key] = 0
        self.freq[key] = self.freq[key] + 1
        return self.cache_data[key]
