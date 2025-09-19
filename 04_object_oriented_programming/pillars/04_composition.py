

""" Composition """

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
        self.running = False

class Lights:
    def __init__(self, type):
        self.type = type
        self.on = False

        
class Car:
    def __init__(self, name, engine: Engine, light: Lights):
        self.name = name
        self.engine = engine

    def start(self):
        self.engine.running = True
        print(f"{self.name} with {self.engine.horsepower} HP engine started.")

    def stop(self):
        self.engine.running = False
        print(f"{self.name} stopped.")


first_vehicle = Car("BMW", Engine(300))
print(first_vehicle.engine.running)
first_vehicle.start()
print(first_vehicle.engine.running)
first_vehicle.stop()
