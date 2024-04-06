class BinarySearch:
    def __init__(self, A):
        self.sa = sorted(A)

    def bin_search(self, x):
        front = 1
        last = len(self.sa) - 1

        while front <= last:
            middle = (front + last) // 2

            if x > self.sa[middle]:
                front = middle + 1
            elif x < self.sa[middle]:
                last = middle - 1
            else:
                return middle

        return -1

def main():
    n = int(input("Enter the number of elements: "))
    A = [int(input(f"Enter element {i + 1}: ")) for i in range(n)]
    bsearch = BinarySearch(A)
    print("The Sorted Element is:", bsearch.sa)

    x = int(input("Enter the element to search: "))
    result = bsearch.bin_search(x)

    if result != -1:
        print(f"Element {x} founded at index {result}.")
    else:
        print(f"Element {x} not found in the array.")

if __name__ == "__main__":
    main()
