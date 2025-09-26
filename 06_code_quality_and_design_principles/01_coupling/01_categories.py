# Tight Coupling

# First example of tight coupling.
# Shared global variables.

pi = 3.14159 # Global variable

def calculate_circle_area(radius):
    return pi * radius * radius

def calculate_circumference(radius):
    return 2 * pi * radius

# Second example of tight coupling.
# Classes directly dependent on each other.

class Engine:
    def start(self):
        return "Engine started"
    
class Car:
    def __init__(self):
        self.engine = Engine()  # Direct dependency on Engine class
    
    def start_car(self):
        return self.engine.start()

   
# Loose Coupling
# First example of loose coupling.
# Using dependency injection.
class Engine:
    def start(self):
        return "Engine started"
    
class Car:
    def __init__(self, engine: Engine):
        self.engine = engine  # Dependency injected via constructor
    
    def start_car(self):
        return self.engine.start()
    

# Second example of loose coupling.
# Functions receiving parameters instead of using globals.

def calculate_circle_area(radius, pi=3.14159):
    return pi * radius * radius

def calculate_circumference(radius, pi=3.14159):
    return 2 * pi * radius
