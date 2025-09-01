


class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

class Profile(User):
    def __init__(self, name, age, bio, location):
        super().__init__(name, age)
        self.bio = bio
        self.location = location

    def get_profile_info(self):
        return f"Name: {self.name}, Age: {self.age}, Bio: {self.bio}, Location: {self.location}"
    
