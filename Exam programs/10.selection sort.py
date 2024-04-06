def selection_sort(list2):
    n = len(list2)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if list2[j] < list2[min_index]:
                min_index = j
        list2[i], list2[min_index] = list2[min_index], list2[i]

    return list2

# Take user input
numlist = list(map(int, input("Enter numbers separated by space: ").split()))

# Call the selection_sort function
sorted_list = selection_sort(numlist)

print("The sorted list is:")
for num in sorted_list:
    print(num, end=" ")
