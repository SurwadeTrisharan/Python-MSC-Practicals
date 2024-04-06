# Using lambda to define an anonymous function
addition = lambda x, y: x + y

# Taking user input for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Using the lambda function to add the numbers
result = addition(num1, num2)
print("Sum of the numbers:", result)
