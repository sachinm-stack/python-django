# Q14.Tuple vs List — Know the Difference


# Q1. Why can't you do t.append(5) if t is a tuple?
# Answer:i because once created value can not change 

# Q2. What is the output of this code and WHY?

t = (10, 20, 30, 20, 10)

print(t.count(20)) # Output: _2__ Why: ___
print(t.index(30)) # Output: _2__ Why: ___
print(max(t)) # Output: _30__
print(min(t)) # Output: __10_
# Q3. In Django, tuples are used for things like URL patterns.
# Give 2 other real-world examples where you'd use a tuple
# instead of a list:
# Example 1:
# Example 2:
# Q4. Convert this list to a tuple, then try to change the first element.
# What error do you get?
nums = [1, 2, 3, 4, 5]
