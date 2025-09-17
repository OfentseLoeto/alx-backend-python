#!/usr/bin/python3
seed = __import__('seed')

def paginate_user(page_size, offset):
    """
    Fetches one 'page' of user in the database.
    - page_size = how many users per page.
    - offset = where to start fetching from (like skiping some rows first)
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows

def lazy_paginate(page_size):
    """
    Connector that lazily fetches pages of users.
    It only goes to the database when you ask for the next page
    Uses 'yield' to give back one page at a time.
    """
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page # Give this page, then pause until called again
        offset += page_size # Move to the next page 