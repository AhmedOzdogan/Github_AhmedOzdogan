user_db = {
    "users": [
        {"id": 1, "name": "Alice" , "password": "password123"},
        {"id": 2, "name": "Bob" , "password": "password456"},
        {"id": 3, "name": "Charlie" , "password": "password789"}
    ]
}

def login(username, password):
    for user in user_db["users"]:
        if user["name"] == username and user["password"] == password:
            return True
    return False


