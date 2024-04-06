 For loop example
print("For loop example:")
for i in range(1, 6):  # Loop from 1 to 5
    print(i, end=" ")  # Print numbers separated by space
print("\n")

# While loop example
print("While loop example:")
count = 1
while count <= 5:  # Loop until count is less than or equal to 5
    print(count, end=" ")  # Print count value
    count += 1  # Increment count by 1
print("\n")

# Using break statement in a loop
print("Using break statement in a loop:")
for i in range(1, 11):  # Loop from 1 to 10
    print(i, end=" ")
    if i == 5:  # If i reaches 5, exit the loop
        break
print("\n")

# Using continue statement in a loop
print("Using continue statement in a loop:")
for i in range(1, 11):  # Loop from 1 to 10
    if i % 2 == 0:  # If i is even, skip to the next iteration
        continue
    print(i, end=" ")
print("\n")

# Nested loop example
print("Nested loop example:")
for i in range(1, 4):  # Outer loop
    for j in range(1, 4):  # Inner loop
        print(f"({i}, {j})", end=" ")  # Print coordinate pairs
    print()  # Print new line after each inner loop
print("\n")

# Using else with loops
print("Using else with loops:")
for i in range(1, 6):  # Loop from 1 to 5
    print(i, end=" ")
else:
    print("Loop completed without using break.")
print("\n")

# While loop with else
print("While loop with else:")
count = 1
while count <= 5:
    print(count, end=" ")
    count += 1
else:
    print("Loop completed without using break.")
