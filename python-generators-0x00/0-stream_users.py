#!/usr/bin/python3
import mysql.connector
import os

DB_HOST = os.getenv("MYSQL_HOST", "localhost")
DB_USER = os.getenv("MYSQL_USER", "prodev_user")
DB_PASS = os.getenv("MYSQL_PASSWORD", "040354a/A")

def stream_users():
    """Generator that fetches rows from the users table one at a time.
       Yield each row as a tuple: (user_id, name, email, age)
    """
    connection = mysql.connector.connect(
        host=localhost,
        user=theo,
        password=040354a/A,
        database=prodev
    )
    cursor = connection.cursor()
    cursor.execute("SELECT user_id, name, email, age FROM user_data")

    for row in cursor:
        yield row
    
    cursor.close()
    connection.close()