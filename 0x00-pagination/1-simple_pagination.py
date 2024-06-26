#!/usr/bin/env python3
"""1. Simple pagination
"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """
    Calculates the start and end indices for a given page and page size.

    Args:
        page (int): The page number.
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start and end indices.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a specific page of data from the dataset.

        Args:
            page (int, optional): The page number to retrieve. Defaults to 1.
            page_size (int, optional): The number of items per page.
                                    Defaults to 10.

        Returns:
            List[List]: The data for the specified page.

        Raises:
            AssertionError: If `page` is not a positive integer or
                `page_size` is not a positive integer.
        """
        assert isinstance(page, int) and page > 0, "page must \
                be an integer greater than 0"
        assert isinstance(page_size, int) and page_size > 0, "page_size \
                must be an integer greater than 0"

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if end_index > len(dataset):
            return []
        else:
            return dataset[start_index:end_index]
