#!/usr/bin/python3
seed = __mport__('seed')

connection = seed.connect_db()
if connection:
    seed.create_database(connection)
    connection.close()
    print(f"connection successful")

    connection = seed.connect_to_prodev()
    if connection:
        seed.create_table(connection)
        seed.insert_data(connection, 'user_data.csv')

        print("Streaming row one by one:")
        for row in seed.stream_row(connection):
            print(row)