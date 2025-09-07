#!/usr/bin/python3
"""
0-stream_users.py
Generator function to stream users row by row from user_data table.
"""

import mysql.connector


def stream_users():
    """Generator that yields user rows one at a time as dictionaries"""
    conn = mysql.connector.connect(
        host="localhost",
        user="Enter db username",          # adjust if needed
        password="Enter db password here",  # adjust if needed
        database="ALX_prodev"
    )
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM user_data")

    # Fetch one row at a time until no more
    row = cursor.fetchone()
    while row:
        yield row
        row = cursor.fetchone()

    cursor.close()
    conn.close()
