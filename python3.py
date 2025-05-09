import hashlib

user_db = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):
    if username in user_db:
        return "Username already exists"
    user_db[username] = hash_password(password)
    return "Created new user"

def login(username, password):
    hashed = hash_password(password)
    if user_db.get(username) == hashed:
        return "Login Successful"
    else:
        return "Invalid credentials"

# Example usage:
print(register("john", "mypassword"))  # Created new user
print(login("john", "mypassword"))     # Login Successful
print(login("john", "wrongpass"))      # Invalid credentials
