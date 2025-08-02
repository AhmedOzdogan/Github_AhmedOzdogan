example_db = {
    "valid_user": "valid_password",
    "current_user": "current_password"
}

def login(username, password):
    if username in example_db and example_db[username] == password:
        return "Login successful"
    return "Login failed"

def register_user(username, password):
    if username in example_db:
        return "Register failed"
    example_db[username] = password
    return "Register successful"