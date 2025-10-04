from typing import Optional, List, Dict, Any
from abc import ABC, abstractmethod

class ICarManagement(ABC):
    @abstractmethod
    def add_car(self, 
                manufacturer: str, 
                model: str, 
                year: str, 
                mileage: int,
                is_available: bool, 
                min_rental_period: int, 
                max_rental_period: int,
                car_rate: float, 
                registration_number: str, 
                car_type: str, 
                fuel_type: str) -> Optional[int]:
        pass

    @abstractmethod
    def update_car(self, 
                   car_id: int, 
                   manufacturer: Optional[str], 
                   model: Optional[str],
                   year: Optional[str], 
                   mileage: Optional[int], 
                   is_available: Optional[bool],
                   min_rental_period: Optional[int], 
                   max_rental_period: Optional[int],
                   car_rate: Optional[float], 
                   registration_number: Optional[str],
                   car_type: Optional[str], 
                   fuel_type: Optional[str]) -> bool:
        pass

    @abstractmethod
    def get_car_by_id(self, car_id: int) -> Optional[Dict[str, Any]]:
        pass

    @abstractmethod
    def get_all_cars(self) -> List[Dict[str, Any]]:
        pass

    @abstractmethod
    def delete_car(self, car_id: int) -> bool:
        pass

    @abstractmethod
    def get_available_cars(self) -> List[Dict[str, Any]]:
        pass

    @abstractmethod
    def close(self) -> None:
        pass