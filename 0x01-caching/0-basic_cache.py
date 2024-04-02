#!/usr/bin/python3
"""0. Basic dictionary
"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    A basic cache implementation that inherits from BaseCaching.

    Attributes:
        cache_data (dict): A dictionary to store key-value pairs.

    Methods:
        put(key, item): Adds a key-value pair to the cache.
        get(key): Retrieves the value associated with the
            given key from the cache.
    """

    def __init__(self):
        """
        Initializes a new instance of the BasicCache class.
        """
        super().__init__()

    def put(self, key, item):
        """
        Adds a key-value pair to the cache.

        Args:
            key: The key to be added.
            item: The value associated with the key.

        Returns:
            None
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve the value associated with the given key from the cache.

        Args:
            key: The key to look up in the cache.

        Returns:
            The value associated with the key, or None if the key is
                not found in the cache.
        """
        if key and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
