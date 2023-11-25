def binary_search(array, value, low, high):
    if high < low:
        return -1
    else:
        mid = (low + high) // 2
        if array[mid] > value:
            return binary_search(array, value, low, mid - 1)  # Fix: Adjust high index for smaller half
        elif array[mid] < value:
            return binary_search(array, value, mid + 1, high)
        else:
            return mid

array = [int(input()) for _ in range(10000)]  # Assuming integer values

for _ in range(10000):
    value = int(input())  # Assuming integer values for queries
    answer = binary_search(array, value, 0, 9999)
    print("%d" % answer)
