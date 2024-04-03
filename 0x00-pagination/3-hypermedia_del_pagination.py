#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        get hyper index
        :param index:
        :param page_size:
        :return:
        """
        assert 0 <= index <= max(self.indexed_dataset().keys()), \
            "invalid range"
        rag = [x for x in self.indexed_dataset().keys() if index <= x]
        next_index = max(sorted(rag)[0: page_size + 1])
        data = [self.indexed_dataset()[x] for x in sorted(rag)[0: page_size]]
        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data
        }
