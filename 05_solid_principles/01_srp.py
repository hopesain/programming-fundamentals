
class BadFileManager:
    def __init__(self, filename: str):
        self.filename = filename
    
    def read(self):
        print(f"Reading from {self.filename}")

    def save(self, data: str):
        print(f"Saving data to {self.filename}")

    def compress(self):
        print(f"Compressing {self.filename}")

    def decompress(self):
        print(f"Decompressing {self.filename}")

    def send_via_email(self, email: str):
        print(f"Sending {self.filename} to {email}")


class FileManager:
    def __init__(self, filename: str):
        self.filename = filename
    
    def read(self):
        print(f"Reading from {self.filename}")

    def save(self, data: str):
        print(f"Saving data to {self.filename}")

class FileCompressor:
    def compress(self, filename: str):
        print(f"Compressing {filename}")

    def decompress(self, filename: str):
        print(f"Decompressing {filename}")


class User:
    def __init__(self, name):
        self.name = name

    def login(self, password):
        print(f"User {self.name} logged in")

    def save_preferences(self, preferences):
        print(f"Saving preferences for {self.name}")


class Authenticator:
    def login(self, user: User, password: str):
        
        print(f"User {user.name} logged in")

    def logout(self, user: User):
        print(f"User {user.name} logged out")