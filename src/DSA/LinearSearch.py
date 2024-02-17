from array import array

def linear_search(arr, value):
    for index, i in enumerate(arr):
        if i == value:
            print("Found at " + str(index))
            return True
    else:
        print("Element not found")
        return False


n = int(input("Enter the number of elements you want to insert: "))
array1 = []
for i in range(n):
    array1.append(int(input("Enter element: ")))

value = int(input("Enter an element to search: "))
linear_search(array1, value)
