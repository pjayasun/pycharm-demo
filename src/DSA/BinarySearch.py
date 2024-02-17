from array import array


def binary_search(arr, value):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2;

        if arr[mid] == value:
            print("Found at " + str(mid))
            return True

        elif arr[mid] > value:
            high = mid-1
        else:
            low = mid+1

    print("Element not found: -1")
    return False
    # for index, i in enumerate(arr):
    #     if i == value:
    #         print("Found at " + str(index))
    #         return True
    # else:
    #     print("Element not found")
    #     return False


n = int(input("Enter the number of elements you want to insert: "))
array1 = []
for i in range(n):
    array1.append(int(input("Enter element: ")))

array1.sort()

value = int(input("Enter an element to search: "))
binary_search(array1, value)
