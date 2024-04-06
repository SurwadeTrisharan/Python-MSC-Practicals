try:
    # Try to perform some operations that may raise specific exceptions
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    result = num1 / num2
    print("Result:", result)
    
    # This operation will raise a ValueError if the input is not an integer
    index = int(input("Enter an index to access a list: "))
    my_list = [1, 2, 3]
    print("Value at index", index, ":", my_list[index])
    
except ZeroDivisionError:
    # Catch division by zero error
    print("Error: Division by zero!")
    
except ValueError:
    # Catch value error (e.g., when converting input to an integer)
    print("Error: Invalid input. Please enter a valid integer.")
    
except IndexError:
    # Catch index error (e.g., when accessing a list with an invalid index)
    print("Error: Index out of range. Please enter a valid index.")
    
except Exception as e:
    # Catch any other exceptions
    print("An error occurred:", e)
