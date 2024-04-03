#!/usr/bin/python3
"""3. LRU Caching
"""


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    A class representing a Least Recently Used (LRU) cache.

    Inherits from BaseCaching.

    Methods:
        __init__(): Initializes an instance of LRUCache.
        put(key, item): Adds an item to the cache.
        get(key): Retrieves the value associated with the given key from the cache.
    """

    def __init__(self):
        """
        Initializes an instance of LRUCache.

        Args:
            None

        Returns:
            None
        """
        super().__init__()

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
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_element = list(self.cache_data.keys())[0]
                del self.cache_data[first_element]
                print(f"DISCARD: {first_element}")

    def get(self, key):
        """
        Retrieves the value associated with the given key from the cache.

        Args:
            key (hashable): The key to look up in the cache.

        Returns:
            The value associated with the key,
            or None if the key is not found in the cache.
        """
        if key and key in self.cache_data.keys():
            value = self.cache_data[key]
            del self.cache_data[key]
            self.cache_data[key] = value
            return value
        return None
