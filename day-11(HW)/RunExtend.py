class Question:

    def __init__(self, text, q_no, question_type, marks):
        self.text = text
        self.q_no = q_no
        self.question_type = question_type
        self.marks = marks

    def display(self):
        print(f"Q{self.q_no}: {self.text} ({self.question_type}, {self.marks} marks)")


class Test:

    def __init__(self, title, teacher):
        self.title = title
        self.teacher = teacher
        self.questions = []
        self.is_published = False

    def add_question(self, question):
        self.questions.append(question)

    def question_count(self):
        return len(self.questions)

    def publish(self):
        if len(self.questions) == 0:
            print("Cannot publish test — no questions added!")
            return
        self.is_published = True
        print(f"Test '{self.title}' published successfully!")

    def show_test(self):
        print(f"\nTest: {self.title}")
        print(f"Teacher: {self.teacher}")
        print(f"Total Questions: {self.question_count()}\n")

        for q in self.questions:
            q.display()


# Demo
q1 = Question("What is Python?", 1, "MCQ", 2)
q2 = Question("Explain OOP.", 2, "Text", 5)

# Extension test
empty_test = Test('Empty Quiz', 'Ravi Sir')

empty_test.publish()   # should fail

empty_test.add_question(q1)
empty_test.publish()   # should succeed

# Add more questions and display
empty_test.add_question(q2)
empty_test.show_test()