def calculator(operation, a, b):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"

operation = input("Enter operation (add, subtract, multiply, divide): ")
a = float(input("Enter first number: "))    
b = float(input("Enter second number: "))
result = calculator(operation, a, b)
print("Result:", result)