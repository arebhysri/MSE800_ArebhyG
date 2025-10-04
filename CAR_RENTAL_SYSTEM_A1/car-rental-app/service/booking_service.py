import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import logging
from Interface.booking_interface import IBookingManagement
from Utils.booking_utils import calculate_price
from Database.database import DatabaseConnection, create_tables

from Enum.bookingAction import BookingAction
from typing import Optional, List, Dict, Any
from datetime import datetime,timedelta
from contextlib import closing
import sqlite3

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class BookingService(IBookingManagement):
    def __init__(self, conn: Optional[sqlite3.Connection] = None):
        self.conn = conn or DatabaseConnection.get_connection()
        create_tables()

    def create_booking(self, car_id: int, user_id: int, start_date: str, end_date: str, car_rate: float) -> Optional[int]:
        price = calculate_price(car_rate, start_date, end_date)
        if price <= 0:
            logger.error("Booking price calculation failed or resulted in zero.")
            return None

        try:
            with closing(self.conn.cursor()) as cursor:
                cursor.execute('''
                    INSERT INTO bookings (car_id, user_id, start_date, end_date, rental_status, price)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (
                    car_id,
                    user_id,
                    start_date,
                    end_date,
                    BookingAction.PENDING.value,
                    price
                ))
                self.conn.commit()
                booking_id = cursor.lastrowid
                logger.info(f"Booking created: ID={booking_id}, Car={car_id}, User={user_id}, Price={price}")
                return booking_id

        except sqlite3.IntegrityError as e:
            logger.error(f"Integrity error while creating booking: {e}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error while creating booking: {e}")
            return 
    
    def update_booking_status(self, booking_id: int, rental_status: str) -> bool:
        if rental_status not in [action.value for action in BookingAction]:
            logger.error("Invalid rental status provided.")
            return False

        try:
            with closing(self.conn.cursor()) as cursor:
                cursor.execute(
                    'UPDATE bookings SET rental_status = ? WHERE booking_id = ?',
                    (rental_status, booking_id)
                )
                self.conn.commit()
                updated = cursor.rowcount > 0
                logger.info(f"Booking {booking_id} status updated to {rental_status}: {updated}")
                return updated

        except Exception as e:
            logger.error(f"Error updating booking status: {e}")
            return False
        
    def get_booking_by_id(self, booking_id: int) -> Optional[dict[str, Any]]:
        try:
            with closing(self.conn.cursor()) as cursor:
                cursor.execute('SELECT * FROM bookings WHERE booking_id = ?', (booking_id,))
                row = cursor.fetchone()
                if row:
                    columns = [column[0] for column in cursor.description]
                    return dict(zip(columns,row))
                return None
        except Exception as e:
            logger.error(f"Error retrieving booking by ID: {e}")
            return None
        
    def get_all_bookings(self) -> List[dict[str,Any]]:
        try:
            with closing(self.conn.cursor()) as cursor:
                cursor.execute('''
                    SELECT bookings.booking_id, bookings.car_id, bookings.user_id,cars.registration_number, cars.model, users.name,
                           bookings.start_date, bookings.end_date, bookings.price, bookings.rental_status
                    FROM bookings
                    INNER JOIN users ON bookings.user_id = users.user_id
                    INNER JOIN cars ON bookings.car_id = cars.car_id
                ''')
                rows = cursor.fetchall()
                columns = [column[0] for column in cursor.description]
                return [dict(zip(columns, row)) for row in rows]
        except Exception as e:
            logger.error(f"Error retrieving all bookings: {e}")
            return []
        
    def delete_booking(self, booking_id: int) -> bool:
        try:
            with closing(self.conn.cursor()) as cursor:
                cursor.execute("DELETE FROM bookings WHERE booking_id = ?", (booking_id,))
                self.conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            logger.error(f"Error deleting booking: {e}")
            return False
        
    def get_bookings_by_user(self, user_id: int) -> List[Dict[str, Any]]:
        try:
            with closing(self.conn.cursor()) as cursor:
                cursor.execute("SELECT * FROM bookings WHERE user_id = ?", (user_id,))
                rows = cursor.fetchall()
                columns = [column[0] for column in cursor.description]
                return [dict(zip(columns, row)) for row in rows]
        except Exception as e:
            logger.error(f"Error retrieving bookings by user ID: {e}")
            return []

    def get_bookings_by_car(self, car_id: int) -> List[Dict[str, Any]]:
        try:
            with closing(self.conn.cursor()) as cursor:
                cursor.execute("SELECT * FROM bookings WHERE car_id = ?", (car_id,))
                rows = cursor.fetchall()
                columns = [column[0] for column in cursor.description]
                return [dict(zip(columns, row)) for row in rows]
        except Exception as e:
            logger.error(f"Error retrieving bookings by car ID: {e}")
            return []
        
    def set_booking_price(self, booking_id: int, price: float) -> bool:
        try:
            with closing(self.conn.cursor()) as cursor:
                cursor.execute("UPDATE bookings SET price = ? WHERE booking_id = ?", (price, booking_id))
                self.conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            logger.error(f"Error setting booking price: {e}")
            return False

    def get_bookings_by_status(self, rental_status: str) -> List[Dict[str, Any]]:
        if rental_status not in BookingAction.__members__.values():
            logger.error("Invalid rental status provided.")
            return []
        try:
            with closing(self.conn.cursor()) as cursor:
                cursor.execute("SELECT * FROM bookings WHERE rental_status = ?", (rental_status,))
                rows = cursor.fetchall()
                columns = [column[0] for column in cursor.description]
                return [dict(zip(columns, row)) for row in rows]
        except Exception as e:
            logger.error(f"Error retrieving bookings by status: {e}")
            return []

    def get_bookings_in_date_range(self, start_date: str, end_date: str) -> List[Dict[str, Any]]:
        try:
            with closing(self.conn.cursor()) as cursor:
                cursor.execute('''
                    SELECT * FROM bookings
                    WHERE (start_date BETWEEN ? AND ?) OR (end_date BETWEEN ? AND ?)
                ''', (start_date, end_date, start_date, end_date))
                rows = cursor.fetchall()
                columns = [column[0] for column in cursor.description]
                return [dict(zip(columns, row)) for row in rows]
        except Exception as e:
            logger.error(f"Error retrieving bookings in date range: {e}")
            return []

    def get_booked_dates(self, car_id: int) -> List[datetime.date]:
        try:
            with closing(self.conn.cursor()) as cursor:
                cursor.execute('''
                    SELECT start_date, end_date FROM bookings
                    WHERE car_id = ? AND rental_status IN (?, ?)
                ''', (car_id, BookingAction.PENDING.value, BookingAction.APPROVE.value))
                rows = cursor.fetchall()

            booked = []
            for start, end in rows:
                start_dt = datetime.strptime(start, "%Y-%m-%d").date()
                end_dt = datetime.strptime(end, "%Y-%m-%d").date()
                booked.extend([
                    start_dt + timedelta(days=i)
                    for i in range((end_dt - start_dt).days + 1)
                ])

            return booked
        except Exception as e:
            logger.error(f"Error fetching booked dates for car {car_id}: {e}")
            return []
    
    def close(self) -> None:
        if self.conn:
            self.conn.close()

    def __del__(self):
        self.close()