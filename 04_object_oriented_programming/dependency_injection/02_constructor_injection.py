from abc import ABC, abstractmethod

class Engine(ABC):
    """ This is the interface for engines in cars. """
    @abstractmethod
    def start(self) -> str:
        pass

class PetrolEngine(Engine):
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return f"Petrol engine with {self.horsepower} HP started"
    
class DieselEngine(Engine):
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return f"Diesel engine with {self.horsepower} HP started"
    
class ElectricEngine(Engine):
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return f"Electric engine with {self.horsepower} HP started"
    

class Transmission(ABC):
    """ This is the interface for transmission in cars. """
    @abstractmethod
    def shift(self) -> str:
        pass

class ManualTransmission(Transmission):
    def shift(self) -> str:
        return "Manual transmission shifted"

class AutomaticTransmission(Transmission):
    def shift(self) -> str:
        return "Automatic transmission shifted"
    

class Car:
    def __init__(self, name: str, engine: Engine, transmission: Transmission):
        self.name = name
        self.engine = engine
        self.transmission = transmission

    def drive(self):
        print(f"Driving {self.name}")
        print(self.engine.start())
        print(self.transmission.shift())


first_car = Car("Toyota", DieselEngine(400), ManualTransmission())
first_car.drive()
