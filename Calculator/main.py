import calculator

def main():

    print("Welcome to your simple Calculator")
    
    try:
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        
        operation = input("Choose an operation ( between : add, subtract, multiply, divide): ").strip().lower()
        
        if operation == 'add':
            result = calculator.add(x, y)
        elif operation == 'subtract':
            result = calculator.subtract(x, y)
        elif operation == 'multiply':
            result = calculator.multiply(x, y)
        elif operation == 'divide':
            result = calculator.divide(x, y)
        else:
            print("Invalid operation.")
            return
        
        print(f"The result is: {result}")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

