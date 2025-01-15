class Student:
    def __init__(self, roll_number, name, age):
        self.roll_number = roll_number
        self.name = name
        self.age = age
        
    def display(self):
        print("Roll Number: ", self.roll_number)
        print("Name: ", self.name)
        print("Age: ", self.age)
        
students = []

students.append(Student(1, "Abhang", 18))
students.append(Student(2, "Bhupesh", 19))
students.append(Student(3, "Chiran", 20))
students.append(Student(4, "Devang", 18))
students.append(Student(5, "Eshant", 19))

for student in students:
    student.display()