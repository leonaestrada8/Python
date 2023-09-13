def calculator(a, b, operation):
    operations = {
        'add': lambda x, y: x + y,
        'subtract': lambda x, y: x - y,
        'multiply': lambda x, y: x * y,
        'divide': lambda x, y: x / y if y != 0 else "Cannot divide by zero",
    }

    return operations.get(operation, "Invalid operation")(a, b)

def get_input():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    operation = input("Enter operation (add, subtract, multiply, divide): ")
    return a, b, operation

a, b, operation = get_input()
result = calculator(a, b, operation)
print("Result:", result)
