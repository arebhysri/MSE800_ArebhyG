import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from service.user_service import UserService
from interface.user_interface import IUserManagement
from database.database import DatabaseConnection
from typing import Optional
import sqlite3
import threading

_lock = threading.Lock()

class UserFactory:
    _instance: Optional[IUserManagement] = None

    @classmethod
    def get_instance(cls) -> IUserManagement:
        if cls._instance is None:
            with _lock:
                if cls._instance is None:
                    cls._instance = UserService(DatabaseConnection().get_connection())
        return cls._instance

    @classmethod
    def create(cls, conn: Optional[sqlite3.Connection] = None) -> IUserManagement:
        # Always returns a fresh instance (useful for testing)
        return UserService(conn or DatabaseConnection().get_connection())

    @classmethod
    def reset(cls):
        # Clears the singleton instance (useful in unit tests)
        with _lock:
            cls._instance = None
