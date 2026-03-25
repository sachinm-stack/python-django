# Q16.Dictionary — Student Management System 


students = {"rahul":90, "john":55, "anita":72, "priya":38, "sara":85}

# 1. Print all student names (keys only)
print(students.keys())

# 2. Print all marks (values only)
print(students.values())

# 3. Print all name-mark pairs using .items()
print(students.items())

# 4. Add a new student: 'ram' with marks 67
students.update({"ram": 67})
print(students)

# 5. Update john's marks to 78 (he improved!)
students.update({"john": 78})
print(students)

# 6. Remove 'priya' from the dictionary
students.pop("priya")
print(students)

# 7. Safe lookup: get marks for 'meera' (not in dict)
# Use .get() with 'Not enrolled' as fallback
print(students.get('meera','not enrolled'))

# 8. Find and print the student with the HIGHEST marks
# (use a for loop to compare — do not use max())
top_student = None
highest_marks = -1   # assuming marks are >= 0

for name, marks in students.items():
    if marks > highest_marks:
        highest_marks = marks
        top_student = name

print("Top student:", top_student)
print("Marks:", highest_marks)

# 9. Count how many students scored above 70
count = 0

for marks in students.values():
    if marks > 70:
        count += 1

print("Students scoring above 70:", count)

# 10. Print a grade report: name → mark → grade (A/B/C/D/F)
students = {"rahul":90, "john":55, "anita":72, "priya":38, "sara":85}

for name, marks in students.items():
    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    elif marks >= 70:
        grade = "C"
    elif marks >= 60:
        grade = "D"
    else:
        grade = "F"
    
    print(name, "→", marks, "→", grade)
