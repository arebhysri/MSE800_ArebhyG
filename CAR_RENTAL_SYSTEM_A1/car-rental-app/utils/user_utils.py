# users_utils.py
import re
import bcrypt

# Regular expression for validating an Email
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
# Regular expression for validating a Password (at least 8 characters, one uppercase, one lowercase, one digit, one special character)
PASSWORD_REGEX = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
SALT_ROUNDS = 12

def validate_email(email: str) -> bool:
    """Validate the email format."""
    return re.match(EMAIL_REGEX, email) is not None 

def validate_password(password: str) -> bool:
    """Validate the password complexity."""
    return re.match(PASSWORD_REGEX, password) is not None   

def hash_password(password: str) -> str:
    """Hash the password using bcrypt."""
    salt = bcrypt.gensalt(SALT_ROUNDS)
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def check_password(password: str, hashed: str) -> bool:
    """Check the password against the hashed value."""
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

