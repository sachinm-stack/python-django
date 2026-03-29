def safe_divide():
    try:
        a = float(input('Enter first number: '))
        b = float(input('Enter second number: '))
        
        result = a / b   # actual operation
        print("Result:", result)

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    except ValueError:
        print("Error: Please enter valid numbers.")

    finally:
        print("Execution completed.")

safe_divide()