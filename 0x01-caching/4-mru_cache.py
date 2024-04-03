#!/usr/bin/python3
"""3. LRU Caching
"""


BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    Most Recently Used (MRU) Cache implementation.

    Inherits from BaseCaching class.

    Attributes:
        cache_data (dict): A dictionary to store key-value pairs.
    """

    def __init__(self):
        """
        Initializes an instance of MRUCache.

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
            if key in self.cache_data.keys():
                del self.cache_data[key]
            if (len(self.cache_data) + 1) > BaseCaching.MAX_ITEMS:
                last_element = list(self.cache_data.keys())[-1]
                del self.cache_data[last_element]
                print(f"DISCARD: {last_element}")
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
        if key and key in self.cache_data.keys():
            value = self.cache_data[key]
            del self.cache_data[key]
            self.cache_data[key] = value
            return value
        return None
