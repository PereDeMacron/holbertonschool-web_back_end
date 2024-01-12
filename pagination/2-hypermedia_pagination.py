#!/usr/bin/env python3
"""simple Pagination"""

from typing import Tuple
import csv
from typing import List


class Server:
    """Servers class for paginating a baby names database."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the Server instance."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Get the cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieve a paginated dataset."""
        assert type(page) == int and page >= 1
        assert type(page_size) == int and page_size >= 1
        pagination = index_range(page, page_size)
        self.dataset()
        return self.__dataset[pagination[0]:pagination[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a dictionary with pagination details."""
        self.dataset()
        total_pages = len(self.dataset())
        data = self.get_page(page, page_size)
        next_page = page + 1 if page + 1 <= total_pages else None
        prev_page = page - 1 if page - 1 >= 1 else None
        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculate the index range for pagination."""
    _tuple = ((page - 1) * page_size, page * page_size)
    return _tuple
