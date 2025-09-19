"""
Liskov Substitution Principle (LSP)

The Liskov Substitution Principle states that objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program.

"""

from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def fly(self):
        raise NotImplementedError("Subclasses must implement this method")
    

class Sparrow(Bird):
    def fly(self):
        return "Sparrow is flying"

class Ostrich(Bird):
    def fly(self):
        raise Exception("Ostriches can't fly")
    

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: float):
        raise NotImplementedError("Subclasses must implement this method")
    
class PayChangu(PaymentMethod):
    def pay(self, amount):
        return f"Paid {amount} using PayChangu"
    
class Malipo(PaymentMethod):
    def pay(self, amount):
        return f"Paid {amount} using Malipo"
    
class Crypto(PaymentMethod):
    def pay(self, amount):
        return f"Paid {amount} using Crypto"
    
class ProcessPayment:
    def process_payment(self, method: PaymentMethod, amount: float):
        if method == Crypto and amount < 200:
            return "Cannot process payment: Minimum amount for Crypto payment is 200"
        return method.pay(amount)
    

first_payment = ProcessPayment()
print(first_payment.process_payment(PayChangu(), 1000))
print(first_payment.process_payment(Malipo(), 500))
print(first_payment.process_payment(Crypto(), 150))
