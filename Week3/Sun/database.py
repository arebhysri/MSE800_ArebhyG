import sqlite3

def create_connection():
    """Create and return a database connection."""
    return sqlite3.connect("users.db")

def create_users_table():
    """Create the users table if it does not exist."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()

def create_students_table():
    """Create the students table if it does not exist."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            stu_id INTEGER PRIMARY KEY AUTOINCREMENT,
            stu_name TEXT NOT NULL,
            stu_address TEXT NOT NULL 
        )
    ''')
    conn.commit()
    conn.close()
