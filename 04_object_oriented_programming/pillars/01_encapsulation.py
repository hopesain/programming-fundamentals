class BankAccount:
    def __init__(self, name, pin):
        self.name = name # Public member.
        self._pin = pin # Protected Member _
        self.__balance = 0 # Private Memmber _ _

    def withdraw(self, amount: int):
        if amount > self.__balance:
            raise ValueError("Insufficent Funds...")
        self.__balance -= amount
        return f"You have withdrawn Mk{amount}. Your new balance is {self.__balance}."
        

    def deposit(self, amount: int):
        if amount <= 0:
            raise ValueError("Deposit amount cannot be less than or equal to zero.")
        self.__balance += amount
        return f"You have received Mk{amount}. Your new balance is Mk{self.__balance}."

    def check_balance(self):
        return f"Your balance is Mk{self.__balance}."

first_account = BankAccount("John Doe", 1234)
print(first_account.check_balance())
print(first_account.deposit(100000))
print(first_account.check_balance())
print(first_account.withdraw(7500))

class Car:
    def __init__(self, name):
        self.name = name 
        self.__engine_status = "off"

    def start(self):
        self.__engine_status = "on"
        return f"The engine of {self.name} is now {self.__engine_status}."

    def stop(self):
        self.__engine_status = "off"
        return f"The engine of {self.name} is now {self.__engine_status}."
    
first_car = Car("Toyota")
print(first_car.start())
print(first_car.stop())
