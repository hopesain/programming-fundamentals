


class User:
    users = []

    def __init__(self, name: str, age: int):
        self.name = name 
        self.age = age #Private member
        User.users.append(self)

    def set_name(self, new_name: str):
        self.name = new_name

    def get_age(self):
        return self.age 
    
    def greet_user(self): #Instance method.
        return f"Good afternoon, {self.name}."
    
    @classmethod #class method.
    def total_users(cls):
        return f"Total number of Users: {len(cls.users)}"
    
    @staticmethod
    def welcome_users():
        return f"Welcome back!"


first_user = User("Hope Sain", 23)
second_user = User("Henry Jamu", 23)
third_user = User("Benjamin", 24)
print(first_user.name)
print(first_user.age)
first_user.set_name("Radson Kaira")
print(f"Display age: {first_user.get_age()}")
print(first_user.name)
print(first_user.greet_user())
print(User.total_users())
print(User.welcome_users())

# All of the above was about Public Members

# The following is about Private Members
# __ before a member makes it private

class BankAccount:
    def __init__(self, account_number: int):
        self.account_number = account_number #Public member 
        self.__balance = 0 #Private member
        self._pin = 1234 #Protected member

    def deposit(self, amount: int):
        self.__balance += amount
        return f"You have deposited '{amount}', your new balance is '{self.__balance}'"

    def get_balance(self):
        return self.__balance
    
first_account = BankAccount(12345)
print(first_account._pin)
print(f"Initial Balance: {first_account.get_balance()}")
print(first_account.deposit(500))
print(f"UpdatedBalance: {first_account.get_balance()}")
