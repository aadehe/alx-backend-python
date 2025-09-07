# #!/usr/bin/python3
# """
# 1-batch_processing.py
# Stream user_data in batches and process each batch with a generator.
# """
#
# import mysql.connector
#
#
# def stream_users_in_batches(batch_size):
#     """
#     Generator: fetches rows in batches from user_data table.
#     """
#     conn = mysql.connector.connect(
#         host="localhost",
#         user="root",          # change if needed
#         password="password",  # change if needed
#         database="ALX_prodev"
#     )
#     cursor = conn.cursor(dictionary=True)
#     cursor.execute("SELECT * FROM user_data")
#
#     while True:
#         batch = cursor.fetchmany(batch_size)
#         if not batch:  # stop when no more rows
#             break
#         yield batch
#
#     cursor.close()
#     conn.close()
#
#
# def batch_processing(batch_size):
#     """
#     Processes each batch: filters users over age 25 and prints them.
#     """
#     for batch in stream_users_in_batches(batch_size):
#         for user in batch:
#             if int(user["age"]) > 25:
#                 print(user)


#!/usr/bin/python3
"""
1-batch_processing.py
Stream user_data in batches and process each batch with a generator.
"""

import mysql.connector


def stream_users_in_batches(batch_size):
    """
    Generator: fetches rows in batches from user_data table.
    """
    conn = mysql.connector.connect(
        host="localhost",
        user="root",          # change if needed
        password="password",  # change if needed
        database="ALX_prodev"
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")

    try:
        while True:
            batch = cursor.fetchmany(batch_size)
            if not batch:
                return "No more rows"   # explicit return at the end
            yield batch
    finally:
        cursor.close()
        conn.close()


def batch_processing(batch_size):
    """
    Processes each batch: filters users over age 25 and prints them.
    """
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if int(user["age"]) > 25:
                print(user)
    return "Batch processing completed"   # added a return here
