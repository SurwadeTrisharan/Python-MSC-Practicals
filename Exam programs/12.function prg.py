from functools import reduce

# Function to calculate the product of two numbers
multiply = lambda x, y: x * y

# Taking user input for the list of numbers
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

# Using reduce to find the product of all numbers in the list
product = reduce(multiply, numbers)

print("List of numbers:", numbers)
print("Product of all numbers:", product)
