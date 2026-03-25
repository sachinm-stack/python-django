# Q15.Set — Deduplication & Operations


# TASK 1 — Remove duplicates from exam results
scores = [88, 72, 95, 88, 61, 72, 100, 88, 95, 61]
# Convert to set to get unique scores
print(set(scores))


# Print: total scores submitted, unique scores, highest, lowest

total_scores = len(scores)
print("Total scores:", total_scores)
print(max(scores))
print(min(scores))


# TASK 2 — Course enrollment analysis
python_students = {"alice","bob","carol","dave","eve"}
django_students = {"carol","dave","frank","grace","eve"}

# Find and print:

# 1. Students enrolled in BOTH courses
print(python_students.union(django_students))

# 2. All unique students across both courses
print(python_students.intersection(django_students))


# 3. Students ONLY in Python (not Django)
redu=python_students-django_students
print(redu)

# 4. Students ONLY in Django (not Python)
redu=django_students-python_students
print(redu)

# 5. Is "alice" in Django? Print True/False
print ( "alice" in django_students)

# 6. Add "harry" to Python course
python_students.add("harry")
print(python_students) 

# 7. Remove 'bob' from Python course safely (use discard)
python_students.discard("bob")
print(python_students)