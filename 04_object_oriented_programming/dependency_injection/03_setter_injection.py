class Engine:
    def __init__(self, horsepower: int):
        self.horsepower = horsepower

class Car:
    def __init__(self, name: str):
        self.name = name
        self.engine = None

    def set_engine(self, engine: Engine):
        self.engine = engine
    
    def start(self):
        if not self.engine:
            print(f"{self.name} cannot start without an engine.")
        print(f"{self.name} with {self.engine.horsepower} HP engine started.")


my_car = Car("Toyota")
print(my_car.engine)
my_car.set_engine(Engine(400))
my_car.start()
