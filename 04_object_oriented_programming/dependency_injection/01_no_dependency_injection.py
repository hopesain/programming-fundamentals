class Engine:
    def start(self):
        return "Engine started"
    

class Car:
    def __init__(self):
        self.engine = Engine()

    def drive(self):
        return self.engine.start()
    
first_car = Car()
print(first_car.drive())
