"""Unit Tests for Register Module"""
import sys
sys.path.insert(0, '..')
from src.auth.register import validate_email, validate_password, register, RegistrationError

def test_validate_email_valid():
    valid, msg = validate_email("test@example.com")
    assert valid == True
    print("test_validate_email_valid passed")

def test_validate_email_invalid():
    valid, msg = validate_email("invalid-email")
    assert valid == False
    print("test_validate_email_invalid passed")

def test_validate_password_weak():
    valid, msgs = validate_password("short")
    assert valid == False
    print("test_validate_password_weak passed")

def test_validate_password_strong():
    valid, msgs = validate_password("StrongPass123")
    assert valid == True
    print("test_validate_password_strong passed")

if __name__ == "__main__":
    test_validate_email_valid()
    test_validate_email_invalid()
    test_validate_password_weak()
    test_validate_password_strong()
    print("\nAll register tests passed!")
