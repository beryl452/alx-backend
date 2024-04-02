#!/usr/bin/python3
"""1. FIFO caching
"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    A First-In, First-Out (FIFO) cache implementation.
    Inherits from the BaseCaching class.

    Attributes:
        cache_data (dict): A dictionary to store the cache data.
    """

    def __init__(self):
        """
        Initializes an instance of FIFOCache.

        Args:
            None

        Returns:
            None
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key (hashable): The key to associate with the item.
            item: The item to be added to the cache.

        Returns:
            None
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_element = list(self.cache_data.keys())[0]
                del self.cache_data[first_element]
                print(f"DISCARD: {first_element}")

    def get(self, key):
        """
        Retrieve the value associated with the given key from the cache.

        Args:
            key (hashable): The key to look up in the cache.

        Returns:
            The value associated with the key,
            or None if the key is not found in the cache.
        """
        if key and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
