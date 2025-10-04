# filepath: c:\Users\Administrator\Documents\GitHub\MSE800_ArebhyG\CAR_RENTAL_SYSTEM_A1\CarRentalSystem\Factory\booking_factory.py

import sys
import os
import threading
import sqlite3
from typing import Optional
import threading

_lock = threading.Lock()

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Service.booking_service import BookingService
from Interface.booking_interface import IBookingManagement
from Database.database import DatabaseConnection

_lock = threading.Lock()

class BookingFactory:
    _instance: Optional[IBookingManagement] = None

    @classmethod
    def get_instance(cls) -> IBookingManagement:
        if cls._instance is None:
            with _lock:
                if cls._instance is None:
                    cls._instance = BookingService(DatabaseConnection().get_connection())
        return cls._instance

    @classmethod
    def create(cls, conn: Optional[sqlite3.Connection] = None) -> IBookingManagement:
        # Always returns a fresh instance (useful for testing or isolated logic)
        return BookingService(conn or DatabaseConnection().get_connection())

    @classmethod
    def reset(cls):
        # Clears the singleton instance (useful in unit tests)
        with _lock:
            cls._instance = None
