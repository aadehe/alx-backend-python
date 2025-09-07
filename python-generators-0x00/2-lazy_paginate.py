#!/usr/bin/python3
"""
2-lazy_paginate.py
Simulate fetching paginated data from user_data using lazy loading.
"""

import seed


def paginate_users(page_size, offset):
    """
    Fetch a single page of users with given page_size and offset.
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows


def lazy_pagination(page_size):
    """
    Generator: yields one page of users at a time lazily.
    Only one loop is used.
    """
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:
            return "No more pages"  # clean stop
        yield page
        offset += page_size
