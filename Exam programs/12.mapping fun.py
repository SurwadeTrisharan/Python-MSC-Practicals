# Using map function to apply a function to each element of a list
numbers = [1, 2, 3, 4, 5]

# Mapping a lambda function to square each element of the list
squared_numbers = list(map(lambda x: x ** 2, numbers))

print("Original list:", numbers)
print("Squared list:", squared_numbers)
