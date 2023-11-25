# Sebastian Lague
def binary_search(array, value, low, high):
    if high < low:
        return -1
    else:
        mid = (low + high)//2
        if array[mid] > value:
            return binary_search(array, value, low, mid-1)
        elif array[mid] < value:
            return binary_search(array, value, mid+1, high)
        else:
            return mid

array = []
for i in range(10000):
    array.append(int(input()))

# Open the file in append mode outside the loop
with open("output2.txt", "a") as output_file:
    for i in range(10000):
        value = int(input())
        answer = binary_search(array, value, 0, 9999)
        print("%d" % answer, file=output_file)

