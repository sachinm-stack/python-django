# 1. DICTIONARY — 5+ students
students = {
    "Rahul": {"maths": 88, "science": 75, "english": 92},
    "gokul": {"maths": 98, "science": 95, "english": 72},
    "balu": {"maths": 85, "science": 60, "english": 70},
    "ajay": {"maths": 70, "science": 65, "english": 60},
    "neha": {"maths": 92, "science": 89, "english": 95}
}

# 2. calculate_average
def calculate_average(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict)

# 3. get_grade
def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

# 4. get_remark
def get_remark(grade):
    if grade == "A":
        return "Excellent"
    elif grade == "B":
        return "Good job"
    elif grade == "C":
        return "Can improve"
    elif grade == "D":
        return "Work harder"
    else:
        return "Needs improvement"

# 5, 6, 7 combined
averages = []
grades_set = set()

for name, subjects in students.items():
    avg = calculate_average(subjects)
    grade = get_grade(avg)
    remark = get_remark(grade)

    averages.append(avg)
    grades_set.add(grade)

    print(f"{name} | Avg: {round(avg,2)} | Grade: {grade} | Remark: {remark}")

# 6. Class stats
class_avg = sum(averages) / len(averages)
highest = max(averages)
lowest = min(averages)

print("\nClass Average:", round(class_avg, 2))
print("Highest Average:", round(highest, 2))
print("Lowest Average:", round(lowest, 2))

# 7. Unique grades
print("Unique Grades:", grades_set)