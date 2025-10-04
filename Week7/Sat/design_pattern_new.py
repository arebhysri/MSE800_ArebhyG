import sqlite3
import threading
import time
from Week7.Sat.database import create_connection  # Ensure this returns a valid SQLite connection

class DatabaseConnection:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._conn = None
        return cls._instance

    def get_connection(self):
        if self._conn is None:
            self._conn = create_connection()
        return self._conn

    def close_connection(self):
        if self._conn:
            self._conn.close()
            self._conn = None

class UserService:
    def __init__(self):
        self.conn = DatabaseConnection().get_connection()

    def insert_user(self, name):
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
            self.conn.commit()
            print(f"Inserted user: {name}")
        except sqlite3.Error as e:
            print(f"Insert error: {e}")

    def get_user(self, user_id):
        start_time = time.time()
        result = None
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
            result = cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            elapsed = time.time() - start_time
            print(f"[UserService_New] Query executed in {elapsed:.6f} seconds")
        return result

class OrderService:
    def __init__(self):
        self.conn = DatabaseConnection().get_connection()

    def insert_order(self, product_name):
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO orders (product_name) VALUES (?)", (product_name,))
            self.conn.commit()
            print(f"Inserted order: {product_name}")
        except sqlite3.Error as e:
            print(f"Insert error: {e}")

    def get_order(self, order_id):
        start_time = time.time()
        result = None
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM orders WHERE id=?", (order_id,))
            result = cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            elapsed = time.time() - start_time
            print(f"[OrderService_New] Query executed in {elapsed:.6f} seconds")
        return result
