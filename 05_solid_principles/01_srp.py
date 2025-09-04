"""
Single Responsibility Principle (SRP)

The Single Responsibility Principle states that a class should have only one reason to change, meaning that a class should only have one job or responsibility.

"""

# SRP Violation

"""
First example:
    We have the file manager class that handles multiple responsibilities such as reading, updating, deleting, compressing, and decompressing files.
"""
class FileManager:
    def __init__(self, file_name: str):
        self.file_name = file_name

    def read(self):
        return f"Reading contents from file '{self.file_name}'"
    
    def update(self):
        return f"Updating contents of file '{self.file_name}'"
    
    def delete(self):
        return f"File deleted."
    
    def compress(self):
        return f"Compressing into a zip file"
    
    def decompress(self):
        return f"Decompressing the file into a readable doc."
    
"""
Reviews about the above example.
The above class has multiple responsibilities.
This is not a good design as the class has multiple reasons to change.
The first group of methods (read, update, delete) are related to file operations, while the second group of methods (compress, decompress) are related to file compression.
Let's split it into two classes:
    1. FileHandler - To handle file operations (read, update, delete)
    2. FileCompressor - To handle file compression task (compress, decompress)
"""

class FileHandler:
    def __init__(self, file_name: str):
        self.file_name = file_name

    def read(self) -> str:
        pass

    def update(self) -> str:
        pass

    def delete(self) -> str:
        pass


class FileCompressor:
    def __init__(self, file_name: str):
        self.file_name = file_name

    def compress(self) -> str:
        pass

    def decompress(self) -> str: 
        pass
    
"""
The second example.
The Report class.
"""
