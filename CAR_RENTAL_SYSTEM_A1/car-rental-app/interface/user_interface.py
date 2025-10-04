from typing import Optional, List, Dict, Any
from abc import ABC, abstractmethod

class IUserManagement(ABC):

    @abstractmethod
    def register_user(self, name: str, 
                      role: str, 
                      email: str, 
                      password: str) -> Optional[int]:
        pass

    @abstractmethod
    def authenticate_user(self, email: str, password: str) -> Optional[Dict[str, Any]]:
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: int) -> Optional[Dict[str, Any]]:
        pass

    @abstractmethod
    def get_all_users(self) -> List[Dict[str, Any]]:
        pass

    @abstractmethod
    def update_user(self, user_id: int, name: Optional[str], role: Optional[str], email: Optional[str], password: Optional[str]) -> bool:
        pass

    @abstractmethod
    def delete_user(self, user_id: int) -> bool:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
