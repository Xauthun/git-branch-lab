"""Unit tests for utils module"""
import sys
sys.path.insert(0, '..')
from src.utils import greet, add

def test_greet():
    assert greet("World") == "Hello, World!"

def test_add():
    assert add(2, 3) == 5

if __name__ == "__main__":
    test_greet()
    test_add()
    print("All tests passed!")
