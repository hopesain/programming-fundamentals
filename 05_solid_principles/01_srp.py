

class BadFile:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        pass

    def write(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def compress(self):
        pass

    def decompress(self):
        pass

    def send_via_emai(self):
        pass

class FileManager:
    def __init__(self, filename):
        self.filename = filename 

    def read(self):
        pass

    def write(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


class FileCompressor:
    def __init__(self, filename, file_location):
        self.filename = filename
        self.file_location = file_location

    def compress(self):
        pass

    def decompress(self):
        pass

class EmailService:
    def send(self, sender, recepient, message, attachment=None):
        pass
