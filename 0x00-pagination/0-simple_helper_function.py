#!/usr/bin/env python3
"""
simple helper funtion
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    index_range
    :param page:
    :param page_size:
    :return:
    """
    return (page - 1) * page_size, page * page_size
