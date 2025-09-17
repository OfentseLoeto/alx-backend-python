#!/usr/bin/python3
import mysql.connector
import os

DB_HOST = os.getenv('MYSL_HOST', 'localhost')
DB_USER = os.getenv('MYSQL_USER', 'theo')
DB_PASS = os.getenv('MYSQL_PASSWORD', 'theo1234')
DB_NAME = os.getenv('MYSQL_DB', 'ALX_prodev')

def stream_users_batches(batch_size):
    """Generator that fetches rows from user_data in batches.
       Each yield gives a list (batch) of rows.
    """
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_id, name, email, age  FROM user_data")
    while True:
        batch = cursor.fetchmany(batch_size)
        if not batch:
            break
        yield batch
    cursor.close()
    connection.closee()

def batch_processing(batch_size):
    """Process user data in batches:
       -Reads batch using stream_users_in_batches
       -Filter user older than 25
       -Prints them
    """
    for batch in stream_users_in_batches(batch_size):
        # fileter users older than 25
        filtered = [user for user in batch if user[3], > 25]
        for user in filtered:
            print(user)