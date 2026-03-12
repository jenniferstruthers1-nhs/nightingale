def add(a, b):
    return a + b

def subtract(a, b):
    return a - b  # <--- fix this in step 7

def multiply(a, b):
    return a * b

def convert_fahrenheit_to_celsius(fahrenheit):
    if fahrenheit < -459.67:
        raise ValueError("Temperature below absolute zero is physically impossible!")
        
    return multiply(subtract(fahrenheit, 32), 5 / 9)