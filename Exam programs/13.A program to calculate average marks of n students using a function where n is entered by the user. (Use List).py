def calculate_average_marks():
    n = int(input("Enter the number of students: "))
    marks = []
    for i in range(n):
        mark = float(input(f"Enter the marks for student {i + 1}: "))
        marks.append(mark)  # Add the mark to the list

    total_marks = sum(marks)
    average = total_marks / n

    print(f"The average marks of {n} students is {average}")

# Call the function
calculate_average_marks()
