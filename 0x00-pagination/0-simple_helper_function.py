#!/usr/bin/env python3
"""
Module with a simple helper function for pagination
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for pagination.
    Page numbers are 1-indexed, i.e. the first page is page 1.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
