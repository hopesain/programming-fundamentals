class User:
    def __init__(self, fullname: str, email: str, age: int):
        self.fullname = fullname
        self.email = email
        self.age = age

    def display_user_information(self):
        return f"Name: {self.fullname}, Email: {self.email}, Age: {self.age}"

class Profile:
    def __init__(self, user: User, bio: str, location: str):
        self.user = user
        self.bio = bio
        self.location = location

    def updated_profile_information(self):
        return f"Bio: {self.bio}, Location: {self.location}, User Info: {self.user.display_user_information()}"

user = Profile(User("John Doe", "john@example.com", 30), "Software Developer", "New York")
print(user.updated_profile_information())