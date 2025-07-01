import mysql.connector
from mysql.connector import Error

try:
   
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='' 
    )

    try:
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    except Error as query_error:
        print(f"Error while executing query: {query_error}")

except Error as conn_error:
    print(f"Error while connecting to MySQL: {conn_error}")

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
