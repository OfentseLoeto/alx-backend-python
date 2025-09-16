#!/usr/bin/python3
import mysql.connector
import csv
import uuid

# Connect to the MySQL database
def connect_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user:"theo",
            password="040354a/A",
        
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    
    # Create the database if not exists
    def create_database(connection):
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
        cursor.close()
    
    # Connect to the ALX_prodev database
    def connect_to_prodev():
        try:
            connection = mysql.connector.connect(
                host="locslhost",
                user="theo",
                password="040354a/A",
                database="ALX_prodev"
            )
            return connecttion
            except mysql.connector.Error as err:
                print(f"Error: {err}")
                return None

# Create the table if not exists
def create_table(connetion):
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users_data (
            user_id CHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL NOT NULL,
            INDEX(user_id)
        )
    """)
    print("Table user_data created successfully")
    cursor.close()

# Insert data from CSV into the table
def insert_data(connection, filename):
    cursor = connection.cursor()
    with open(filename, newline='') as csvfile:
        reader = csvDictReader(csvfile)
        for row in reader:
            user_id = str(uuid.uuid4())
            name = row['name']
            email = row['email']
            age = row['age']

            # Checking if email aready exists to avoid duplicates
            cursor.execute("SELECT * FROM userdata WHERE email = %s", (email,))
            result = cursor.fetchone()
            if not result:
                cursor.execute("""
                    INSERT INTO user_data (user_id, name, email, age)
                    VALUES (%s, %s, %s, %s)
                """, (user_id, name, email, age)
                )
    connection.commit()
    cursor.close()

# Generator that streams rows one by one
def stream_data(connection):
    cursor = connection.cursor(dictionary=true)
    cursor.execute("SELECT * FROM user_data")

    for row in cursor:
        yield row

    cursor,close()