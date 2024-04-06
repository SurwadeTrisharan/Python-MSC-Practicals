# main.py

# Method 1: Import the module directly
#import calculator

# Method 2: Import the module and rename it
import calculator as calc

# Method 3: Import specific functions from the module
from calculator import add as addition, subtract as subtraction, multiply as multiplication, divide as division

# Get user input for numbers
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

# Using the module directly
print("\nUsing the calculator module directly:")
print("Addition:", calculator.add(x, y))
print("Subtraction:", calculator.subtract(x, y))
print("Multiplication:", calculator.multiply(x, y))
print("Division:", calculator.divide(x, y))

# Using the module with a renamed alias
print("\nUsing the calculator module with a renamed alias:")
print("Addition:", calc.add(x, y))
print("Subtraction:", calc.subtract(x, y))
print("Multiplication:", calc.multiply(x, y))
print("Division:", calc.divide(x, y))

# Using specific functions from the module
print("\nUsing specific functions from the calculator module:")
print("Addition:", addition(x, y))
print("Subtraction:", subtraction(x, y))
print("Multiplication:", multiplication(x, y))
print("Division:", division(x, y))
