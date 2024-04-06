def bubble_sort(list1):
    n=len(list1)
    for i in range(n):  
        for j in range(0,n-i-1):
            if list1[j]>list1[j+1]:
                list1[j], list1[j+1] = list1[j+1],list1[j]
numlist = list(map(int, input("Enter numbers separated by space: ").split()))

sorted_list=bubble_sort(numlist)
print("The sorted list is:")
for i in range(len(numlist)):
    print(numlist[i], end=" ")
