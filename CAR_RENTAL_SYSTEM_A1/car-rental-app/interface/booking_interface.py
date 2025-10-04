from typing import Optional, List, Dict, Any
from abc import ABC, abstractmethod
import datetime

class IBookingManagement(ABC):

    @abstractmethod
    def create_booking(self, car_id: int, user_id: int, start_date: str, end_date: str, car_rate: float) -> Optional[int]: pass

    @abstractmethod
    def update_booking_status(self, booking_id: int, rental_status: str) -> bool: pass

    @abstractmethod
    def get_booking_by_id(self, booking_id: int) -> Optional[Dict[str, Any]]: pass

    @abstractmethod
    def get_all_bookings(self) -> List[Dict[str, Any]]: pass

    @abstractmethod
    def delete_booking(self, booking_id: int) -> bool: pass

    @abstractmethod
    def get_bookings_by_user(self, user_id: int) -> List[Dict[str, Any]]: pass

    @abstractmethod
    def get_bookings_by_car(self, car_id: int) -> List[Dict[str, Any]]: pass

    @abstractmethod
    def set_booking_price(self, booking_id: int, price: float) -> bool: pass

    @abstractmethod
    def get_bookings_by_status(self, rental_status: str) -> List[Dict[str, Any]]: pass

    @abstractmethod
    def get_bookings_in_date_range(self, start_date: str, end_date: str) -> List[Dict[str, Any]]: pass

    @abstractmethod
    def get_booked_dates(self, car_id: int) -> List[datetime.date]: pass

    @abstractmethod
    def close(self) -> None:
        pass
