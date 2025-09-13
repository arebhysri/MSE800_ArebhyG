import sqlite3

def create_connection():
    """Create a database connection to the SQLite database."""
    return sqlite3.connect("order.db")

def create_tables():
    """Create users and orders tables if they do not exist."""
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()