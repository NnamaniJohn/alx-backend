#!/usr/bin/env python3
"""
simple pagination
"""
import csv
from typing import List
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    index_range
    :param page:
    :param page_size:
    :return:
    """
    return (page - 1) * page_size, page * page_size


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        init
        """
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
        get page
        :param page:
        :param page_size:
        :return:
        """
        assert type(page) is int, "Page must be a number"
        assert type(page_size) is int, "Page size must be a number"
        assert page > 0 and page_size > 0, \
            "Page or Page size must be greater than zero"
        start, stop = index_range(page, page_size)
        try:
            self.dataset()
            return self.__dataset[start: stop]
        except IndexError:
            return []
