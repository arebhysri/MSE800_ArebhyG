import sqlite3
from database import create_connection 
import time

class UserService:

    def __init__(self):
        self.conn = create_connection()
        self.cursor = self.conn.cursor()

    def insert_user(self, name):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
        self.conn.commit()
        self.conn.close()

    def get_user(self, user_id):
        start_time = time.time()
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
            result = cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            result = None
        finally:
            end_time = time.time()
            print(f"Query executed in {end_time - start_time:.6f} seconds")
        self.conn.close()
        return result
    
class OrderService:

    def __init__(self):
        self.conn = create_connection()
        self.cursor = self.conn.cursor()

    def insert_order(self, product_name):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO orders (product_name) VALUES (?)", (product_name,))
        self.conn.commit()
        self.conn.close()

    def get_order(self, order_id):
        start_time = time.time()
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM orders WHERE id=?", (order_id,))
            result = cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            result = None
        finally:
            end_time = time.time()
            print(f"Query executed in {end_time - start_time:.6f} seconds")
        self.conn.close()
        return result

