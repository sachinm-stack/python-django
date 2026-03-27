# For each code snippet below, predict the output WITHOUT running it. Then run to verify.

# Snippet A:
a = [10, 20, 30]
b = a
b.append(99)
print(a)
print(b)

# Your predicted output: ____________a,b same output:10,20,30,99___________________

# Snippet B:
a = [10, 20, 30]
b = a.copy()
b.append(99)
print(a)
print(b)

# Your predicted output: _____________a=10,20,30/10,20,30,99__________________

# Snippet C:
a = [10, 20, 30]
b = a
b = [40, 50, 60]      # redeclaration
b.append(70)
print(a)
print(b)

# Your predicted output: ________a=10,20,30  /  b=40,50,60,70_______________________

# Hint: Snippet A: b = a makes both point to the SAME list. Snippet B: .copy() creates an independent list. Snippet C: b = [40, 50, 60] is redeclaration — b now points to a new list, so a is untouched.

