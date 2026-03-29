class User:

    def __init__(self, first_name, last_name, age):
        """Initialize the user."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0
    
jason_bigsby = User("Jason", "Bigsby", 3000)
print(f"{jason_bigsby.first_name} {jason_bigsby.last_name}")
print(f"Age: {jason_bigsby.age}")       

jason_bigsby.increment_login_attempts()
jason_bigsby.increment_login_attempts()
jason_bigsby.increment_login_attempts()
jason_bigsby.increment_login_attempts()
jason_bigsby.increment_login_attempts()
print(f"Login attempts: {jason_bigsby.login_attempts}")
jason_bigsby.reset_login_attempts()
print(f"Login attempts after reset: {jason_bigsby.login_attempts}")
