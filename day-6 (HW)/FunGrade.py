student={"rahul":90,"gokul":70,"mak":55,"aak":39}
def  get_grade(marks):
    if marks >=80:
        return ("A Grade")
    elif marks >=60:
        return ("B Grade")
    elif marks >=40:
        return ("C Grade")
    elif marks <=39:
        return ("D Grade")
for name,marks in student.items():
    grade=get_grade(marks)
    print(name,"->",grade)


