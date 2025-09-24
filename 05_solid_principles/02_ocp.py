from abc import ABC, abstractmethod

STORED_PASSWORD = "1234"
STORED_PATTERN = "L"
STORED_FINGERPRINT = "F"


class BadScreenLock:
    def __init__(self):
        self.is_locked = True

    def unlock_screen(self, unlock_method, password=None, pattern=None, fingerprint=None):
        if unlock_method == "password":
            if password == STORED_PASSWORD:
                self.is_locked = False
                return "Screen Unlocked"
            self.is_locked = True
            return "Incorrect Password"
        elif unlock_method == "pattern":
            if pattern == STORED_PATTERN:
                self.is_locked = False
                return "Screen Unlocked"
            self.is_locked = True
            return "Incorrect Pattern"
        elif unlock_method == "fingerprint":
            if fingerprint == STORED_FINGERPRINT:
                self.is_locked = False
                return "Screen Unlocked"
            self.is_locked = True
            return "Incorrect Fingerprint"
        
        
""" Unlock Strategy Interface """
class UnlockStrategy(ABC):
    @abstractmethod
    def unlock(self):
        pass

class PasswordStrategy(UnlockStrategy):
    def unlock(self, credential):
        if not credential == STORED_PASSWORD:
            raise Exception("Incorrect Password")
        return True

class PatternStrategy(UnlockStrategy):
    def unlock(self, credential):
        if not credential == STORED_PATTERN:
            raise Exception("Incorrect Pattern")
        return True
    
class FingerprintStrategy(UnlockStrategy):
    def unlock(self, credential):
        if not credential == STORED_FINGERPRINT:
            raise Exception("Incorrect Fingerprint")
        return True

class ScreenLock:
    def __init__(self):
        self.is_locked = True

    def unlock_screen(self, strategy: UnlockStrategy, credential):
        if strategy.unlock(credential):
            self.is_locked = False
            return "Screen Unlocked"
        self.is_locked = True
        return "Unlock Failed"
    

"""
Second Example:
Suppose we have a system that accepts payments through various payment gateways like paychangu, pawapay, malipo and others.
In some instances, we might need to add new payment gateways to the system or remove existing ones when they are no longer supported.
Your first instinct may be to throw a bunch of if-else statements to handle the different payment gateways.
This may work but at what cost?
You will end up with a large, monolithic class that is difficult to maintain and extend.

I will first demonstrate the bad approach using if-else statements.
Then I will show you how to refactor the code to adhere to the Open/Closed Principle using polymorphism and interfaces.
"""


""" 
Bad Approach:
As you are assessing the stated problem, you will notice that we have common behavior across the different payment gateways.
Which is to process payments. The required parameters and logic may be different but the behavior is the same.

Parameters: amount, payment_method, others.
"""
class BadPaymentProcessor:
    def __init__(self):
        self.__is_payment_successful = False
    
    def process_payment(self, payment_gateway, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than zero")
        
        if payment_gateway == "paychangu":
            """ Add complex logic here to process payment via paychangu """
            self.__is_payment_successful = True
            return "Payment Successful"
        
        elif payment_gateway == "pawapay":
            """ Add complex logic here to process payment via pawapay """
            self.__is_payment_successful = True
            return "Payment Successful"
        
        elif payment_gateway == "malipo":
            """ Add complex logic here to process payment via malipo """
            self.__is_payment_successful = True
            return "Payment Successful"
        
        else:
            self.__is_payment_successful = False
            return "Payment Failed: Unsupported Payment Gateway"
        
"""
Now what if it gets worse, each payment gateway has multiple payment methods.
For example, paychangu supports mobile money and card payments.
This will make the code even more complex and harder to maintain.


Now let's refactor the code to adhere to the Open/Closed Principle.
We will create an interface for the payment gateway and implement it for each payment gateway.
We will use polymorphism since each payment gateway has a different implementation of the process_payment method.
"""

class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount):
        raise NotImplementedError("Child classes must implement this method")
    
class PayChangu(PaymentGateway):
    def process_payment(self, amount):
        """ Add complex logic here to process payment via paychangu """
        return "Payment Successful via PayChangu"
    
class PawaPay(PaymentGateway):
    def process_payment(self, amount):
        """ Add complex logic here to process payment via pawapay """
        return "Payment Successful via PawaPay"
    
class Malipo(PaymentGateway):
    def process_payment(self, amount):
        """ Add complex logic here to process payment via malipo """
        return "Payment Successful via Malipo"

class PaymentProcessor:
    def __init__(self):
        self.__is_payment_successful = False

    def make_payment(self, payment_gateway: PaymentGateway, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than zero")
        
        result = payment_gateway.process_payment(amount)
        self.__is_payment_successful = True

        return result


""" Client Code """
if __name__ == "__main__":
    bad_lock = BadScreenLock()
    print(bad_lock.unlock_screen("password", password="1234"))
    print(bad_lock.unlock_screen("pattern", pattern="X")) 
    print(bad_lock.unlock_screen("fingerprint", fingerprint="F"))

    print("====================================")

    good_lock = ScreenLock()
    print(good_lock.unlock_screen(PasswordStrategy(), "1234"))  
    print(good_lock.unlock_screen(PatternStrategy(), "L"))  
    print(good_lock.unlock_screen(FingerprintStrategy(), "F"))  

    print("====================================")
    bad_payment_processor = BadPaymentProcessor()
    print(bad_payment_processor.process_payment("paychangu", 100))
    print(bad_payment_processor.process_payment("pawapay", 200))
    print(bad_payment_processor.process_payment("malipo", 300))
    print(bad_payment_processor.process_payment("unknown_gateway", 400))

    print("====================================")
    good_payment_processor = PaymentProcessor()
    print(good_payment_processor.make_payment(PayChangu(), 100))
    print(good_payment_processor.make_payment(PawaPay(), 200))
    print(good_payment_processor.make_payment(Malipo(), 300))
    # print(good_payment_processor.make_payment("unknown_gateway", 400)) # This will raise an error since the argument is not of type PaymentGateway.
