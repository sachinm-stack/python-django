class Question:
    def __init__(self, text,q_no,question_type,marks):
        self.text           =text
        self.q_no           =q_no
        self.question_type =question_type
        self.marks         = marks
    
    def print_values(self):
        print(f"Q{self.q_no}:{self.text}({self.question_type},{self.marks}marks)")
    
q1=Question("wht is pyhton?",1,"mcq",2)
q2=Question("Explain OOP.",2,"text",5)
print(q1.text)
print(q2.question_type)

q2.marks =4
q1.print_values()
q1.print_values()
