visitors = ["alice","bob","alice","carol","bob","dave","alice"]
print(visitors.__len__())
unique=set(visitors)
print(unique)
print(unique.__len__())

# if "eve" in visitors:
#     print("yes",visitors)
# else:
#     print("no")

print("eve" in visitors)

# if "bob" in visitors:
#     print("yes",visitors)
# else:
#     print("no")

print("bob" in visitors)
