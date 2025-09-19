stored_password = "1234"
stored_pattern = "L"

class BadScreenLock:
    def __init__(self):
        self.__is_device_locked = True

    def lock(self):
        self.__is_device_locked = True
        return f"Your device is locked"
    
    def unlock(self, unlock_method, password: str = None, pattern: str = None):
        if self.__is_device_locked:
            if unlock_method == "password":
                if password == stored_password:
                    self.__is_device_locked = False
                    return "Your device is unlocked"
                raise ValueError("Incorrect password")
            elif unlock_method == "pattern":
                if pattern == stored_pattern:
                    self.__is_device_locked = False
                    return "Your device is unlocked"
                raise ValueError("Incorrect pattern")
            raise ValueError("Unsupported unlock method")
        return "Your device is already unlocked"
    

from abc import ABC, abstractmethod

class UnlockMethod(ABC):
    @abstractmethod
    def unlock(self):
        raise NotImplementedError("Subclasses must implement this method")

class PasswordMethod(UnlockMethod):
    def __init__(self, password: str):
        self.password = password

    def unlock(self):
        if self.self.password == stored_password:
            return True
        raise ValueError("Incorrect password")
    
class PatternMethod(UnlockMethod):
    def __init__(self, pattern: str):
        self.pattern = pattern

    def unlock(self):
        if self.pattern == stored_pattern:
            return True
        raise ValueError("Incorrect pattern")
    

class GoodScreenLock:
    def __init__(self):
        self.__is_device_locked = True

    def lock_screen(self):
        self.__is_device_locked = True
        return f"Your device is locked"
    
    def unlock_screen(self, method: UnlockMethod):
        if self.__is_device_locked:
            if method.unlock():
                self.__is_device_locked = False
                return "Your device is unlocked"
        return "Your device is already unlocked"
    
# Example usage:
bad_lock = BadScreenLock()
print(bad_lock.unlock("password", password="1234"))
print(bad_lock.lock())

good_lock = GoodScreenLock()
print(good_lock.unlock_screen(PatternMethod("L")))
print(good_lock.lock_screen())
