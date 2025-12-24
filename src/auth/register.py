import re
from datetime import datetime


class RegistrationError(Exception):
    pass


def validate_email(email: str):
    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    if re.match(pattern, email):
        return True, "Email valid"
    return False, "Invalid email format"


def validate_password(password: str):
    msgs = []

    if len(password) < 8:
        msgs.append("Password must be at least 8 characters")
    if not any(ch.islower() for ch in password):
        msgs.append("Password must contain lowercase letter")
    if not any(ch.isupper() for ch in password):
        msgs.append("Password must contain uppercase letter")
    if not any(ch.isdigit() for ch in password):
        msgs.append("Password must contain a number")

    if msgs:
        return False, msgs
    return True, ["Password valid"]


def register(username: str, email: str, password: str):
    email_valid, email_msg = validate_email(email)
    if not email_valid:
        raise RegistrationError(email_msg)

    pass_valid, pass_msgs = validate_password(password)
    if not pass_valid:
        raise RegistrationError(", ".join(pass_msgs))

    user = {
        "username": username,
        "email": email,
        "created_at": datetime.now().isoformat(),
        "is_active": True,
    }

    print(f"Registration successful: {username}")
    return user

