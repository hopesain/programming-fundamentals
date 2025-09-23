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


if __name__ == "__main__":
    bad_lock = BadScreenLock()
    print(bad_lock.unlock_screen("password", password="1234"))
    print(bad_lock.unlock_screen("pattern", pattern="X")) 
    print(bad_lock.unlock_screen("fingerprint", fingerprint="F"))

    print("------------------------------------")

    good_lock = ScreenLock()
    print(good_lock.unlock_screen(PasswordStrategy(), "1234"))  
    print(good_lock.unlock_screen(PatternStrategy(), "S"))  
    print(good_lock.unlock_screen(FingerprintStrategy(), "F"))  