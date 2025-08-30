from typing import Dict

class User:
    users = []

    def __init__(self, fullname: str, username: str, email: str, password: str) -> Dict:
        self.fullname = fullname
        self.username = username
        self.email = email
        self.password = password
        User.users.append(self) # Store the user instance in the class variable

    def get_user_information(self) -> Dict:
        """ This method returns the user information as a dictionary. """
        return {
            "fullname": self.fullname,
            "username": self.username,
            "email": self.email,
            "password": self.password
        }
    
    @classmethod
    def get_users(cls):
        return [user.get_user_information() for user in cls.users]


first_user = User("John Doe", "johndoe", "john@example.com", "securepassword")
second_user = User("Jane Smith", "janesmith", "jane@example.com", "anothersecurepassword")
print(first_user.get_user_information())
print(User.get_users())


class Timer:
    DEFAULT_TIMEOUT = 10 # 

    @classmethod
    def set_default_timeout(cls, timeout: int):
        cls.DEFAULT_TIMEOUT = timeout
        return cls.DEFAULT_TIMEOUT


initiate_timer = Timer()
print(Timer.DEFAULT_TIMEOUT)
set_timeout = initiate_timer.set_default_timeout(20)
print(Timer.DEFAULT_TIMEOUT)


