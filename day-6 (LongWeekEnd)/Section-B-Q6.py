# Q6. Type Conversion Errors

# Each code block below has a bug related to type conversion or concatenation. Identify the error, explain WHY it happens, and fix it.
# There are 4 bugs total.


# BUG 1 — find and fix:

print("My age is: " +" 25")

# Error: ________str try to  add with int so str concadinate with only str 25 not with int___ Fix: ____"25"_______

# BUG 2 — find and fix:

age = int(input("Age: "))
print("Next year: ",age + 1)
# Error: ________here also 1 is int it cant concadinate so change tostr then run ___ Fix: ______str(1)_____
# BUG 3 — find and fix:
x = int("3")
# Error: _____here int should number not str ______ Fix: _____three to 3______
# BUG 4 — find and fix:
num = int(input("Enter number: "))
result = num * 2
print("Double:", result) # user types 5, but prints 55 not 10
# Error: _____we didnt mention it should int so it consider it as str ______ Fix: ______num = int(input("Enter number: "))_____