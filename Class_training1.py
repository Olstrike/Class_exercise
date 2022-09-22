#oliver stafferöd
#TEINF-20

class Person:
    def __init__(self, name, age, gender) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    def get_name(self):
        self.name = input("What's your name?: ")

    

class Student(Person):
    def __init__(self, name, age, gender, classes: list):
        super().__init__(name, age, gender)
        self.classes = classes



class Teacher(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

class Course:
    def __init__(self, name, students: list, teachers: list):
        self.name = name
        self.students = students
        self.teachers = teachers