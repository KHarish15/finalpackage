def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    # ERROR HANDLING: Check for division by zero
    # This prevents the program from crashing when someone tries to divide by 0
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def multiply(a, b):
    return a * b

def is_even(n):
    return n % 2 == 0

def get_max(numbers):
    # ERROR HANDLING: Check for empty list
    # This prevents the program from crashing when someone passes an empty list
    if not numbers:
        raise ValueError("Empty list provided")
    return max(numbers) 