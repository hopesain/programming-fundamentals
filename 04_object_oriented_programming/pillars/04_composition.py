class Engine:
    def __init__(self, engine_type: str, horsepower: int):
        self.engine_type = engine_type
        self.horsepower = horsepower
        self.is_engine_on = False

    def start_engine(self):
        """ This methods starts the engine of the vehicle """
        self.is_engine_on = True
        return f"Your {self.engine_type} engine with {self.horsepower} HP is now running."
    
    def stop_engine(self):
        """ This method stops the engine of the vehicle """
        self.is_engine_on = False
        return f"Your {self.engine_type} engine with {self.horsepower} HP is now stopped."
    

class Car:
    def __init__(self, engine: Engine ):
        self.engine = engine

    def start_car(self):
        return self.engine.start_engine()


first_car = Car(Engine("V8", 400))
print(first_car.start_car())