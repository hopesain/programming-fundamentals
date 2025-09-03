class Engine:
    def start(self):
        return f"Engine started"
    
class Car:
    def __init__(self):
        self.engine = None

    def set_engine(self, engine: Engine):
        self.engine = engine

    def drive(self):
        """ 
        This function implements the drive behaviour in vehicles

        Args:
            None

        Returns:
            str: A message indicating the engine has started

        Exceptions:
            NotImplementedError: If the engine is not set

        Example:
            car = Car()
            car.set_engine(Engine())
            car.drive()
        """
        if self.engine is None:
            raise NotImplementedError("Engine not set")
        return self.engine.start()
    
first_car = Car()
first_car.set_engine(Engine())
print(first_car.drive())