"""
Register Module
New user registration system
"""

import re
from datetime import datetime

class RegistrationError(Exception):
    """Exception for registration errors"""
    pass

def validate_email(email):
    """Validate email format"""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True, "Email valid"
    return False, "Invalid email format"

def validate_password(password):
    """Validate password strength"""
    errors = []
    if len(password) < 8:
        errors.append("Password must be at least 8 characters")
    if not any(c.isupper() for c in password):
        errors.append("Password must contain uppercase letter")
    if not any(c.isdigit() for c in password):
        errors.append("Password must contain a number")

    if errors:
        return False, errors
    return True, ["Password valid"]

def register(username, email, password):
    """Register new user"""
    email_valid, email_msg = validate_email(email)
    if not email_valid:
        raise RegistrationError(email_msg)

    pass_valid, pass_msgs = validate_password(password)
    if not pass_valid:
        raise RegistrationError(", ".join(pass_msgs))

    user = {
        'username': username,
        'email': email,
        'created_at': datetime.now().isoformat(),
        'is_active': True
    }

    print(f"Registration successful: {username}")
    return user
