import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from interface.car_interface import ICarManagement
from utils.car_utils import logger
from database.database import DatabaseConnection, create_tables
from typing import Optional, List, Dict, Any
from datetime import datetime
from contextlib import closing
import sqlite3

class CarService(ICarManagement):
    def __init__(self, conn: Optional[sqlite3.Connection] = None):
        self.conn = conn or DatabaseConnection.get_connection()
        create_tables()

    def add_car(self, manufacturer: str, model: str, year: str, mileage: int,
                is_available: bool, min_rental_period: int, max_rental_period: int,
                car_rate: float, registration_number: str,car_type:str, fuel_type:str ) -> Optional[int]:
        created_at = datetime.now().isoformat()
        last_update = created_at
        is_available = 1 if is_available else 0

        try:
            with closing(self.conn.cursor()) as cursor:
                cursor.execute('''
                    INSERT INTO cars (manufacturer, model, year, 
                               mileage, is_available,min_rental_period,
                               max_rental_period, car_rate,registration_number,
                               car_type,fuel_type,last_update,
                                      created_at)
                    VALUES (?, ?, ?,  ?, ?, ?,  ?, ?, ?,  ?, ?, ?,  ?)
                ''', (manufacturer, model, year, 
                      mileage, is_available,min_rental_period, 
                      max_rental_period, car_rate,registration_number,
                      car_type,fuel_type,last_update,created_at))
                self.conn.commit()
                return cursor.lastrowid
        except sqlite3.IntegrityError as e:
            logger.error(f"Integrity error while adding car: {e}")
            return None
        except Exception as e:
            logger.error(f"Error while adding car: {e}")
            return None

    def update_car(self, car_id: int, manufacturer: Optional[str], model: Optional[str],
                   year: Optional[str], mileage: Optional[int], is_available: Optional[bool],
                   min_rental_period: Optional[int], max_rental_period: Optional[int],
                   car_rate: Optional[float],car_type: Optional[str], 
                   fuel_type: Optional[str],registration_number: Optional[str]) -> bool:
        updates = []
        params = []

        if manufacturer:
            updates.append("manufacturer = ?")
            params.append(manufacturer)
        if model:
            updates.append("model = ?")
            params.append(model)
        if year:
            updates.append("year = ?")
            params.append(year)
        if mileage is not None:
            updates.append("mileage = ?")
            params.append(mileage)
        if is_available is not None:
            updates.append("is_available = ?")
            params.append(1 if is_available else 0)
        if min_rental_period is not None:
            updates.append("min_rental_period = ?")
            params.append(min_rental_period)
        if max_rental_period is not None:
            updates.append("max_rental_period = ?")
            params.append(max_rental_period)
        if car_rate is not None:
            updates.append("car_rate = ?")
            params.append(car_rate)
        if car_type is not None:
            updates.append("car_type = ?")
            params.append(car_type)
        if fuel_type is not None:
            updates.append("fuel_type = ?")
            params.append(fuel_type)
        if registration_number is not None:
            updates.append("registration_number = ?")
            params.append(registration_number)

        if not updates:
            logger.warning("No updates provided for car.")
            return False

        updates.append("last_update = ?")
        params.append(datetime.now().isoformat())
        params.append(car_id)
        sql = f"UPDATE cars SET {', '.join(updates)} WHERE car_id = ?"

        try:
            with closing(self.conn.cursor()) as cursor:
                cursor.execute(sql, params)
                self.conn.commit()
                return cursor.rowcount > 0
        except sqlite3.IntegrityError as e:
            logger.error(f"Integrity error while updating car: {e}")
            return False
        except Exception as e:
            logger.error(f"Error while updating car: {e}")
            return False

    def delete_car(self, car_id: int) -> bool:
        try:
            with closing(self.conn.cursor()) as cursor:
                cursor.execute("DELETE FROM cars WHERE car_id = ?", (car_id,))
                self.conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            logger.error(f"Error while deleting car: {e}")
            return False

    def get_car_by_car_id(self, car_id: int) -> Optional[Dict[str, Any]]:
        try:
            with closing(self.conn.cursor()) as cursor:
                cursor.execute("SELECT * FROM cars WHERE car_id = ?", (car_id,))
                row = cursor.fetchone()
                if row:
                    columns = [column[0] for column in cursor.description]
                    return dict(zip(columns, row))
                return None
        except Exception as e:
            logger.error(f"Error while retrieving car: {e}")
            return None

    def list_cars(self, available_only: bool = False) -> List[Dict[str, Any]]:
        try:
            with closing(self.conn.cursor()) as cursor:
                query = "SELECT * FROM cars WHERE is_available = 1" if available_only else "SELECT * FROM cars"
                cursor.execute(query)
                rows = cursor.fetchall()
                columns = [column[0] for column in cursor.description]
                return [dict(zip(columns, row)) for row in rows]
        except Exception as e:
            logger.error(f"Error while listing cars: {e}")
            return []

    def set_car_availability(self, car_id: int, is_available: bool) -> bool:
        is_available_int = 1 if is_available else 0
        try:
            with closing(self.conn.cursor()) as cursor:
                cursor.execute('''
                    UPDATE cars
                    SET is_available = ?, last_update = ?
                    WHERE car_id = ?
                ''', (is_available_int, datetime.now().isoformat(), car_id))
                self.conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            logger.error(f"Error while setting car availability: {e}")
            return False

    def get_all_cars(self) -> List[Dict[str, Any]]:
        try:
            with closing(self.conn.cursor()) as cursor:
                cursor.execute("SELECT * FROM cars")
                rows = cursor.fetchall()
                columns = [column[0] for column in cursor.description]
                return [dict(zip(columns, row)) for row in rows]
        except Exception as e:
            logger.error(f"Error retrieving all cars: {e}")
            return []

    def get_available_cars(self) -> List[Dict[str, Any]]:
        try:
            with closing(self.conn.cursor()) as cursor:
                cursor.execute("SELECT * FROM cars WHERE is_available = 1")
                rows = cursor.fetchall()
                columns = [column[0] for column in cursor.description]
                return [dict(zip(columns, row)) for row in rows]
        except Exception as e:
            logger.error(f"Error retrieving available cars: {e}")
            return []

    def get_car_by_id(self, car_id: int) -> Optional[Dict[str, Any]]:
        try:
            with closing(self.conn.cursor()) as cursor:
                cursor.execute("SELECT * FROM cars WHERE car_id = ?", (car_id,))
                row = cursor.fetchone()
                if row:
                    columns = [column[0] for column in cursor.description]
                    return dict(zip(columns, row))
                return None
        except Exception as e:
            logger.error(f"Error retrieving car by ID: {e}")
            return None

    def close(self) -> None:
        if self.conn:
            self.conn.close()

    def __del__(self):
        self.close()
