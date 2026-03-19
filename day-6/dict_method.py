students={
    "rahul":90,
    "anita":85
}

print(students)
print(type(students))

print("\n")
students["john"]=90
print(students)

print("\n")
students["rahul"]=95
print(students)

students.update({"rahul":100})
print(students)

print(students.get("rahul"))

print(students.get("maria"))

print(students.get("maria","not found"))

print(students.keys())
print(students.values())
print(students.items())

students.pop("anita")
print(students)

students.popitem()
print(students)

students.clear()
print(students)