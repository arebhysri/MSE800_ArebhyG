import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from interface.user_interface import IUserManagement
from utils.user_utils import validate_email, validate_password, hash_password, check_password
from database.database import DatabaseConnection, create_tables
from enums.usre_role import user_role
from typing import Optional, List, Dict, Any
from datetime import datetime
from contextlib import closing
import sqlite3
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class UserService(IUserManagement):
    def __init__(self, conn: Optional[sqlite3.Connection] = None):
        self.conn = conn or DatabaseConnection.get_connection()
        create_tables()

    def register_user(self, name: str, role: str, email: str, password: str) -> Optional[int]:
        if role not in [user_role.ADMIN, user_role.CUSTOMER]:
            logger.error("Invalid role provided.")
            return None
        if not validate_email(email):
            logger.error("Invalid email format.")
            return None
        if not validate_password(password):
            logger.error("Password does not meet complexity requirements.")
            return None

        hashed = hash_password(password)
        created_at = datetime.now().isoformat()

        try:
            with closing(self.conn.cursor()) as cursor:
                cursor.execute('''
                    INSERT INTO users (name, role, email, password, created_at)
                    VALUES (?, ?, ?, ?, ?)
                ''', (name, role, email, hashed, created_at))
                self.conn.commit()
                return cursor.lastrowid
        except sqlite3.IntegrityError as e:
            logger.error(f"Integrity error: {e}")
            return None
        except Exception as e:
            logger.error(f"Error registering user: {e}")
            return None

    def authenticate_user(self, email: str, password: str) -> Optional[Dict[str, Any]]:
        try:
            with closing(self.conn.cursor()) as cursor:
                cursor.execute('SELECT user_id, name, role, email, password FROM users WHERE email = ?', (email,))
                user = cursor.fetchone()
                if user and check_password(password, user[4]):
                    last_login = datetime.now().isoformat()
                    cursor.execute('UPDATE users SET last_login = ? WHERE user_id = ?', (last_login, user[0]))
                    self.conn.commit()
                    return {
                        'user_id': user[0],
                        'name': user[1],
                        'role': user[2],
                        'email': user[3],
                        'last_login': last_login
                    }
                return None
        except Exception as e:
            logger.error(f"Error during authentication: {e}")
            return None

    def get_user_by_id(self, user_id: int) -> Optional[Dict[str, Any]]:
        try:
            with closing(self.conn.cursor()) as cursor:
                cursor.execute('SELECT user_id, name, role, email, created_at, last_login FROM users WHERE user_id = ?', (user_id,))
                user = cursor.fetchone()
                if user:
                    return dict(zip([column[0] for column in cursor.description], user))
                return None
        except Exception as e:
            logger.error(f"Error retrieving user by ID: {e}")
            return None

    def get_all_users(self) -> List[Dict[str, Any]]:
        try:
            with closing(self.conn.cursor()) as cursor:
                cursor.execute('SELECT user_id, name, role, email, created_at, last_login FROM users')
                rows = cursor.fetchall()
                columns = [column[0] for column in cursor.description]
                return [dict(zip(columns, row)) for row in rows]
        except Exception as e:
            logger.error(f"Error retrieving all users: {e}")
            return []

    def update_user(self, user_id: int, name: Optional[str], role: Optional[str], email: Optional[str], password: Optional[str]) -> bool:
        updates = []
        params = []

        if name:
            updates.append("name = ?")
            params.append(name)
        if role:
            if role not in [user_role.ADMIN, user_role.CUSTOMER]:
                logger.error("Invalid role provided.")
                return False
            updates.append("role = ?")
            params.append(role)
        if email:
            if not validate_email(email):
                logger.error("Invalid email format.")
                return False
            updates.append("email = ?")
            params.append(email)
        if password:
            if not validate_password(password):
                logger.error("Password does not meet complexity requirements.")
                return False
            updates.append("password = ?")
            params.append(hash_password(password))

        if not updates:
            logger.warning("No updates provided.")
            return False

        updates.append("last_login = ?")
        params.append(datetime.now().isoformat())
        params.append(user_id)

        sql = f"UPDATE users SET {', '.join(updates)} WHERE user_id = ?"

        try:
            with closing(self.conn.cursor()) as cursor:
                cursor.execute(sql, params)
                self.conn.commit()
                return cursor.rowcount > 0
        except sqlite3.IntegrityError as e:
            logger.error(f"Integrity error: {e}")
            return False
        except Exception as e:
            logger.error(f"Error updating user: {e}")
            return False

    def delete_user(self, user_id: int) -> bool:
        try:
            with closing(self.conn.cursor()) as cursor:
                cursor.execute('DELETE FROM users WHERE user_id = ?', (user_id,))
                self.conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            logger.error(f"Error deleting user: {e}")
            return False

    def close(self) -> None:
        if self.conn:
            self.conn.close()

    def __del__(self):
        self.close()
