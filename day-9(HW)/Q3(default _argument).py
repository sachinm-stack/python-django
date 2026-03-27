def calculate(a, b, operation="add"):
    operation = operation.lower()
    
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            return "Cannot divide by zero"
        return a / b
    else:
        return "Invalid operation"

# Test cases
print(calculate(10, 5))                    # 15
print(calculate(10, 5, "subtract"))        # 5
print(calculate(10, 5, "multiply"))        # 50
print(calculate(10, 5, "divide"))          # 2.0
print(calculate(10, 0, "divide"))          # Cannot divide by zero
print(calculate(b=5, a=20))                # 25
