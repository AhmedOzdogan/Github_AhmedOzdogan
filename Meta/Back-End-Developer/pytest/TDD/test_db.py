import pytest
from db import login,example_db,register_user

def test_login_valid_credentials():
    assert login("valid_user", "valid_password") == "Login successful"

def test_login_wrong_password():
    assert login("valid_user", "wrong_password") == "Login failed"

def test_login_invalid_user():
    assert login("invalid_user", "valid_password") == "Login failed"


def test_register_user():
    assert register_user("current_user", "current_password") == "Register failed"


# TDD means we write tests before the actual implementation.
# In traditional testing, we write tests after the implementation.