import calculator

print("Welcome to your simple Calculator")

try:
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input. Please enter numeric values.")
    exit()

operation = input("Choose an operation (add, subtract, multiply, divide): ").strip().lower()

if operation == 'add':
    result = calculator.add(x, y)
elif operation == 'subtract':
    result = calculator.subtract(x, y)
elif operation == 'multiply':
    result = calculator.multiply(x, y)
elif operation == 'divide':
    try:
        result = calculator.divide(x, y)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        exit()
else:
    print("Invalid operation.")
    exit()

print(f"The result is: {result}")
