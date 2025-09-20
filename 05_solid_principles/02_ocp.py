
SAVED_PASSWORD = "1234"
SAVED_PATTERN = "L"
SAVED_FINGERPRINT = "F"

class BadScreenLock:
    def __init__(self):
        self.__is_device_locked = True

    def unlock_screen(self, unlock_method, password=None, pattern=None, fingerprint=None, face_recognition=None):
        if unlock_method == "Password":
            if password == SAVED_PASSWORD:
                self.__is_device_locked = False
                return f"Your device is now unlocked."
            self.__is_device_locked = True
            return f"Incorrect password."
        elif unlock_method == "Pattern":
            if pattern == SAVED_PATTERN:
                self.__is_device_locked = False
                return f" Your device is now unlocked."
            return f"Incorrect pattern."
        elif unlock_method == "fingerprint":
            if pattern == SAVED_FINGERPRINT:
                self.__is_device_locked = False
                return f" Your device is now unlocked."
            return f"Incorrect fingerprint."
        
    
    def lock_screen(self):
        self.__is_device_locked = True
        return f"Your device is locked."
    

first_unlock = ScreenLock()
print(first_unlock.unlock_screen("Password", password="1237"))


