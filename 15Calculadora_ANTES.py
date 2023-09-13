# ANTES DA REFATORAÇÃO:

def calculator(a, b, operation):
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
            return "Cannot divide by zero"
    else:
        return "Invalid operation"

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (add, subtract, multiply, divide): ")

result = calculator(a, b, operation)
print("Result:", result)
