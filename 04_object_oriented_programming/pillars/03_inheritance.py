

class ParentClass:
    def __init__(self, first_attribute, second_attribute):
        self.first_attribute = first_attribute
        self.second_attribute = second_attribute

class ChildClass(ParentClass):
    def __init__(self, first_attribute, second_attribute, unique_attribute):
        super.__init__(first_attribute, second_attribute)
        self.unique_attribute = unique_attribute


class User:
    def __init__(self, fullname, age):
        self.fullname = fullname
        self.age = age

    def greet_user(self):
        return f"Good evening, '{self.fullname}'"
    
class Student(User):
    def __init__(self, fullname, age, student_id):
        super().__init__(fullname, age)
        self.student_id = student_id

    def student_information(self):
        return f"Student ID: {self.student_id}, Name: {self.fullname}, Age: {self.age}"

class Lecturer:
    pass


first_student = Student("Taonga Zimba", 20, "adc123")
print(first_student.greet_user())
print(first_student.student_information())