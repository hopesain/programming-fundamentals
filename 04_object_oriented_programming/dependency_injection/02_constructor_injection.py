class Engine:
    def __init__(self, horsepower: int):
        self.horserpower = horsepower

class Car:
    def __init__(self, name: str, engine: Engine):
        self.engine = engine 
        self.name = name 

    def start(self):
        print(f"{self.name} with {self.engine.horserpower} HP engine started.")
