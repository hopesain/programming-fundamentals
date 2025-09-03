"""
No Dependency Injection

In this example, the Car class is tightly coupled with the Engine class.

"""

class Engine:
    def start(self) -> str:
        return "Engine started"
    

class Car:
    def __init__(self):
        self.engine = Engine()

    def drive(self):
        return self.engine.start()
    
first_car = Car()
print(first_car.drive())
