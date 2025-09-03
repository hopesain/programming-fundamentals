"""
Method Injection

This forwards dependencies straight to the required method.

In this case, the Car class does not hold a reference to the Engine class. Instead, the Engine instance is passed directly to the drive method when needed.

"""

class Engine:
    def start(self):
        return f"Engine started."
    
class Car:
    def drive(self, engine: Engine):
        """ 
        This function implements the drive behaviour in vehicles

        Args:
            engine (Engine): An instance of the Engine class

        Returns:
            str: A message indicating the engine has started
        """
        return engine.start()
    
first_car = Car()
print(first_car.drive(Engine()))