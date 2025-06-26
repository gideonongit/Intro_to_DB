import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )

        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    create_database()
