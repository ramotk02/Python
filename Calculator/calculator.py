def add(a,b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
 try:
        return a / b
 except ZeroDivisionError:
        raise ValueError("Cannot divide by zero")    