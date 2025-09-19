
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

def animal_sound(animal: Animal):
    animal.speak()

cat = animal_sound(Cat())
dog = animal_sound(Dog())