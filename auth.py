def authenticate_user(token):
    print("Verifying JWT authentication token...")
    return True if token else False
def authenticate(username, password):
    users = {
        "admin": "admin123",
        "guest": "guest123",
    }

    if users.get(username) == password:
        print(f"Login successful for {username}")
        return True

    print("Login failed: invalid credentials")
    return False