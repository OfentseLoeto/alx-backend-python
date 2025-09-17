#!/usr/bin/python3
import seed

def stream_user_ages():
    """
    Generator that yield user ages one by one from the database.
    Uses 'yield' so that it doesn't load everything at once.
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor()
    cursor.execute("SELECT age FROM user_data")
    for (age,) in cursor:
        yield age
    cursor.close()
    connection.close()

def calculate_average_age():
    """
    Use the generator stream_user_ages() to calculate the avarage age.
    Keep only total sum + count in memory, not the whole dataset.
    """
    total = 0
    count = 0

    for age in stream_user_ages():
        total += age
        count += 1

    if count == 0:
        print("No user found")
    else:
        avarage = total / count
        print(f"Avarage age of users: {avarage:.2f}") 