def add(a, b):
    return a + b

def subtract(a, b):
    return a - b  # <--- fix this in step 7

def multiply(a, b):
    return a * b

def convert_fahrenheit_to_celsius(fahrenheit):
    # Fixed: Changed 9/5 to 5/9
    return multiply(subtract(fahrenheit, 32), 5 / 9)