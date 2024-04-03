#!/usr/bin/python3
"""5. LFU Caching
"""
from collections import OrderedDict
import time


BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    Least Frequently Used (LFU) Cache implementation.

    This class inherits from the BaseCaching class and provides methods for
    putting items into the cache and retrieving items from the cache based on
    the LFU eviction policy.

    Attributes:
        frequencies (dict): A dictionary to keep track
            of the frequencies of cache items.
        timestamps (OrderedDict): An ordered dictionary to keep track of
            the timestamps of cache items.

    Methods:
        put(key, item): Puts an item into the cache with the specified key.
        get(key): Retrieves the item from the cache with the specified key.

    """

    def __init__(self):
        super().__init__()
        self.frequencies = {}
        self.timestamps = OrderedDict()

    def put(self, key, item):
        """
        Puts an item into the cache with the specified key.

        If the key already exists in the cache,
            its frequency is incremented and
        its timestamp is updated. If the cache is full,
            the least frequently used
        item is evicted based on the LFU eviction policy.

        Args:
            key: The key of the item to be put into the cache.
            item: The item to be put into the cache.

        Returns:
            None

        """

        if key is None or item is None:
            return

        if key in self.cache_data:
            self.frequencies[key] += 1
            self.timestamps.move_to_end(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lfu_key = min(self.frequencies, key=self.frequencies.get)
                if (self.frequencies[lfu_key]
                        == [self.frequencies[key]
                            for key in self.frequencies]):
                    lfu_key = self.timestamps.popitem(last=False)[0]
                print("DISCARD:", lfu_key)
                del self.cache_data[lfu_key]
                del self.frequencies[lfu_key]
                del self.timestamps[lfu_key]

            self.frequencies[key] = 1
            self.timestamps[key] = time.time()

        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves the item from the cache with the specified key.

        If the key does not exist in the cache,
        None is returned. Otherwise, the
        item is returned and its timestamp is updated.

        Args:
            key: The key of the item to be retrieved from the cache.

        Returns:
            The item associated with the specified key,
            or None if the key does not exist in the cache.

        """

        if key is None or key not in self.cache_data:
            return None

        self.timestamps.move_to_end(key)
        return self.cache_data[key]
