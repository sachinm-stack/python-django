# Part A — Integer
a = 10
print(id(a))    # ID 1
a = a + 5
print(id(a))    # ID 2 — same or different?

# Part B — List
L = [1, 2, 3]
print(id(L))    # ID 3
L.append(4)
print(id(L))    # ID 4 — same or different?

# Part C — String
s = "hello"
print(id(s))    # ID 5
s = s + " world"
print(id(s))    # ID 6 — same or different?

# Write your predictions:
# ID 1 vs ID 2: ____immutable _______  Reason: _________int can change value so it store other space__________________
# ID 3 vs ID 4: ____mutable_______  Reason: __________list will update in same location_________________
# ID 5 vs ID 6: _____immutable______  Reason: _________str also store in other space__________________
