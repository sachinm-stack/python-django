class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display(self):
        print(f"Name: {self.name} | Age: {self.age} | Grade: {self.grade}")


# Create 3 student objects and call display() on each
s1 = Student('Rahul', 20, 'A')
s2 = Student('Anita', 22, 'B')
s3 = Student('John', 21, 'C')

s1.display()
s2.display()
s3.display()