class Student:

    def __init__(self, name, marks):
        self.name  = name
        self.marks = marks

    def grade(self):
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 75:
            return 'B'
        elif self.marks >= 60:
            return 'C'
        elif self.marks >= 50:
            return 'D'
        else:
            return 'F'


class Classroom:

    def __init__(self, subject, teacher):
        self.subject  = subject
        self.teacher  = teacher
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def class_summary(self):
        print(f"Subject: {self.subject}")
        print(f"Teacher: {self.teacher}")
        print("Students:")

        for student in self.students:
            print(f"{student.name} → Grade: {student.grade()}")


# Test it:
s1 = Student('Rahul', 90)
s2 = Student('Anita', 72)
s3 = Student('John',  55)

python_class = Classroom('Python', 'Ravi Sir')
python_class.add_student(s1)
python_class.add_student(s2)
python_class.add_student(s3)

python_class.class_summary()