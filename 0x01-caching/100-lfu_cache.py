#!/usr/bin/python3
"""5. LFU Caching
"""


BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    Least Frequently Used (LFU) Cache implementation.

    Inherits from BaseCaching class.

    Attributes:
        _frequency (dict): A dictionary to keep track
            of the frequency of each key.

    Methods:
        put(key, item): Adds an item to the cache.
        get(key): Retrieves the value associated
            with the given key from the cache.
    """

    def __init__(self):
        """
        Initializes an instance of LFUCache.

        Args:
            None

        Returns:
            None
        """
        super().__init__()
        self._frequency = {}

    def put(self, key, item):
        """
        Adds an item to the cache.

        Args:
            key (hashable): The key to associate with the item.
            item: The item to be added to the cache.

        Returns:
            None
        """
        if key and item:
            if (len(self.cache_data) >= BaseCaching.MAX_ITEMS and
                    key not in self.cache_data.keys()):
                min_freq = min(self._frequency.values())
                keys = [k for k, v in self._frequency.items() if v == min_freq]
                if len(keys) == 1:
                    del self.cache_data[keys[0]]
                    del self._frequency[keys[0]]
                else:
                    min_key = None
                    for k in self.cache_data.keys():
                        if min_key is None and k in keys:
                            min_key = k
                            break
                    if min_key:
                        del self.cache_data[min_key]
                        del self._frequency[min_key]
                        print(f"DISCARD: {min_key}")
            if key in self.cache_data.keys():
                del self.cache_data[key]
                self._frequency[key] += 1
            else:
                self._frequency[key] = 1
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves the value associated with the given key from the cache.

        Args:
            key (hashable): The key to look up in the cache.

        Returns:
            The value associated with the key,
            or None if the key is not found in the cache.
        """
        if key in self.cache_data.keys():
            self._frequency[key] += 1
            value = self.cache_data[key]
            del self.cache_data[key]
            self.cache_data[key] = value
            return value
        return None
