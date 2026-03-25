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

STATUS_CHOICES = (
    ('P', 'Pending'),
    ('C', 'Completed'),
    ('F', 'Failed'),
)

Why tuple?
Because these values are fixed constants. If someone accidentally modifies them at runtime, your database logic breaks. Tuple prevents that.

# Example 2:

ALLOWED_HOSTS = ('localhost', '127.0.0.1')
These are configuration constants. You don’t want some random part of your code doing:

# Q4. Convert this list to a tuple, then try to change the first element.
# What error do you get?
nums = [1, 2, 3, 4, 5]
print(tuple(nums))
nums.insert(1,6)
print(nums)
