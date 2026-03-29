# Q17.Function Anatomy



# Save as: section_f.py
# 1. Complete this function — returns the square of a number
def square(n):
    return n
# ___________
print(square(5)) # Expected: 25
print(square(12)) # Expected: 144


# 2. Complete this function — returns the larger of two numbers
def find_max(a, b):
    if a>b:
        return a
    else:
        return b
print(find_max(10, 20)) # Expected: 20
print(find_max(99, 3)) # Expected: 99


# 3. Complete this — returns True if a number is even, False if odd
def is_even(n):
    if n % 2==0:
        return True
    else :
        return False

print(is_even(4)) # Expected: True
print(is_even(7)) # Expected: False