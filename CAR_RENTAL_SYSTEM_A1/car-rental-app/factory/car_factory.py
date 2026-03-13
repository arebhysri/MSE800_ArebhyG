import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from service.car_service import CarService
from service.car_service import ICarManagement
from database.database import DatabaseConnection
import sqlite3
import threading
from typing import Optional

_lock = threading.Lock()

class CarFactory:
    _instance: Optional[ICarManagement] = None

    @classmethod
    def get_instance(cls) -> ICarManagement:
        if cls._instance is None:
            with _lock:
                if cls._instance is None:
                    cls._instance = CarService(DatabaseConnection().get_connection())
        return cls._instance

    @classmethod
    def create(cls, conn: Optional[sqlite3.Connection] = None) -> ICarManagement:
        return CarService(conn or DatabaseConnection().get_connection())

    @classmethod
    def reset(cls):
        with _lock:
            cls._instance = None
