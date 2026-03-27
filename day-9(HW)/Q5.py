x = 50

def change_x():
    x = 99         # local x — does NOT affect global
    print("Inside:", x)

change_x()
print("Outside:", x)

# Your predicted output: ______inside is 99 and outside is 50_________________________


count = 0

def add_one():
    global count
    count += 1

add_one()
add_one()
add_one()
print(count)


# Your predicted output: ____________idk___________________
# output :3



items = ["apple", "banana"]

def add_item(lst):
    lst.append("cherry")   # modifies the original list

add_item(items)
print(items)


# Your predicted output: ____________idk___________________
# output :['apple', 'banana', 'cherry']
