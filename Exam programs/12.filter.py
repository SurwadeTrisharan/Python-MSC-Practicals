numbers = list(map(int,input("Enter the numbers in seperated by space").split()))
even_numbers = list(filter(lambda x: x % 2 == 0,numbers))

print("Original list:", numbers)
print("Even numbers:", even_numbers)
