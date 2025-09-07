#!/usr/bin/python3
"""
3-average_age.py
Compute average age using a generator (memory-efficient).
"""

import seed


def stream_user_ages():
    """
    Generator: yields user ages one at a time from the DB.
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT age FROM user_data")

    for row in cursor:
        yield int(row["age"])   # yield ages lazily

    cursor.close()
    connection.close()


def calculate_average_age():
    """
    Consume the generator to compute average age without loading everything into memory.
    """
    total = 0
    count = 0
    for age in stream_user_ages():  # only one loop
        total += age
        count += 1

    if count > 0:
        average = total / count
        print(f"Average age of users: {average:.2f}")
    else:
        print("No users found")
