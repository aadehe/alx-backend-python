#!/usr/bin/env python3
"""
seed.py - Set up ALX_prodev database, create user_data table,
and populate it with CSV data.
"""

import mysql.connector
import csv
import uuid


# -------------------------------
# 1. Connect to MySQL server
# -------------------------------
def connect_db():
    """Connect to MySQL server (without selecting a database)."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="Enter db username here",          # Change if different
            password="Enter db password here"   # Change to your MySQL root password
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        exit(1)


# -------------------------------
# 2. Create database if not exists
# -------------------------------
def create_database(connection):
    """Create ALX_prodev database if it does not exist."""
    cursor = connection.cursor()
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        print("Database ALX_prodev is ready.")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")
        exit(1)
    cursor.close()


# -------------------------------
# 3. Connect to ALX_prodev
# -------------------------------
def connect_to_prodev():
    """Connect to the ALX_prodev database."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="Enter db username here",          # Change if needed
            password="Enter db password here",  # Change if needed
            database="ALX_prodev"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        exit(1)


# -------------------------------
# 4. Create table user_data
# -------------------------------
def create_table(connection):
    """Create user_data table if it does not exist."""
    cursor = connection.cursor()
    table_sql = """
    CREATE TABLE IF NOT EXISTS user_data (
        user_id CHAR(36) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        age DECIMAL(3,0) NOT NULL,
        INDEX (user_id)
    )
    """
    cursor.execute(table_sql)
    connection.commit()
    cursor.close()
    print("Table user_data is ready.")


# -------------------------------
# 5. Insert data into table
# -------------------------------
def insert_data(connection, data):
    """
    Insert a single row into user_data if not exists.
    data = (user_id, name, email, age)
    """
    cursor = connection.cursor()
    check_sql = "SELECT user_id FROM user_data WHERE user_id = %s"
    cursor.execute(check_sql, (data[0],))
    result = cursor.fetchone()

    if not result:
        insert_sql = "INSERT INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_sql, data)
        connection.commit()
        print(f"Inserted {data[1]} ({data[2]})")
    else:
        print(f"User {data[1]} already exists, skipping...")

    cursor.close()


# -------------------------------
# 6. Generator to stream rows
# -------------------------------
def stream_user_data(connection):
    """Generator that yields user_data rows one by one."""
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")
    for row in cursor:
        yield row
    cursor.close()


# -------------------------------
# 7. Main logic
# -------------------------------
if __name__ == "__main__":
    # Step 1: Connect to server & create DB
    conn = connect_db()
    create_database(conn)
    conn.close()

    # Step 2: Connect to ALX_prodev
    conn = connect_to_prodev()
    create_table(conn)

    # Step 3: Read CSV and insert data
    with open("user_data.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            user_id = str(uuid.uuid4())  # Generate UUID for user_id
            data = (user_id, row["name"], row["email"], row["age"])
            insert_data(conn, data)

    # Step 4: Stream rows using generator
    print("\nStreaming rows from user_data:")
    for row in stream_user_data(conn):
        print(row)

    conn.close()
