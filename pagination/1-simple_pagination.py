#!/usr/bin/env python3
"""simle pagination"""
from typing import Tuple
import csv
import math
from typing import List


class Server:
    """
    simples pagination
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        simple pagination
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """simple pagination"""
        assert type(page) == int and page >= 1
        assert type(page_size) == int and page_size >= 1
        pagination = index_range(page, page_size)
        self.dataset()
        return self.__dataset[pagination[0]:pagination[1]]


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """simple pagination"""
    _tuple = ((page - 1) * page_size, page * page_size)
    return _tuple
