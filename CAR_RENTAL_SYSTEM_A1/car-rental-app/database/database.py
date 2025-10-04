import sqlite3
import threading

class DatabaseConnection:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        # Prevent reinitialization in singleton
        if not hasattr(self, '_initialized'):
            self._connection = None
            self._initialized = True  

    def get_connection(self):
        if self._connection is None:
            self._connection = sqlite3.connect(
                'car_rental_App.db',
                check_same_thread=False,
                timeout=30
            )
        return self._connection
    
    def close_connection(self):
        if self._connection:
            self._connection.close()
            self._connection = None


# Create tables if they do not exist
def create_tables():
    conn = DatabaseConnection().get_connection()
    cursor = conn.cursor()
    
    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            role TEXT CHECK(role IN ('admin', 'customer')) NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            created_at TEXT NULL,
            last_login TEXT
        )
    ''')
    
    # Create cars table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cars (
            car_id INTEGER PRIMARY KEY AUTOINCREMENT,
            manufacturer TEXT NOT NULL,
            model TEXT NOT NULL,
            year TEXT NOT NULL,
            mileage INTEGER NOT NULL,
            is_available INTEGER CHECK(is_available IN (0, 1)) NOT NULL,
            min_rental_period INTEGER NOT NULL,
            max_rental_period INTEGER NOT NULL,
            car_rate REAL NOT NULL,
            registration_number TEXT UNIQUE NOT NULL,
            car_type TEXT NOT NULL,
            fuel_type TEXT NOT NULL,
            created_at TEXT NOT NULL,
            last_update TEXT NOT NULL
        )
    ''')
    
    # Create bookings table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            booking_id INTEGER PRIMARY KEY,
            car_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            registration_number TEXT NULL,
            start_date TEXT NOT NULL,
            end_date TEXT NOT NULL,
            rental_status TEXT NOT NULL CHECK(rental_status IN ('pending', 'approved', 'rejected', 'completed')),
            price REAL NULL,
            FOREIGN KEY(car_id) REFERENCES cars(car_id),
            FOREIGN KEY(user_id) REFERENCES users(user_id)
        )
    ''')
    
    conn.commit()
    # do not close here; let the singleton manage the connection
