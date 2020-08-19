
#
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# n = 7
# you want to check some index in this array
# mid = high + low / 2
# check element at index mid
#

def binary_search(arr, n):
    """
    search n in array and return its index, if you find, return -1
    :param arr: sorted list of numbers
    :param n: number to find
    :return: index of n or -1
    """
    low = 0
    high = len(arr) - 1

    found = False
    index = -1     # error condition

    # integer overflow, int, float, double

    while not found and low <= high:
        # mid = (low + high) // 2
        mid = low + ((high - low) // 2) # integer overflow cases for big numbers

        # print(f"mid = {mid}")

        if arr[mid] == n:
            found = True
            index = mid
        elif arr[mid] < n:  # you have to check right side
            low = mid + 1
        else:               # check left side
            high = mid - 1

        # print(f"low={low}, high={high}")

    return index

numbers = [-10, -9, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21] # sorted
# array/list
num = 18
print(f"Index of {num} is ", binary_search(numbers, num))
num = 11  # edge case
print(f"Index of {num} is ", binary_search(numbers, num))
num = 21  # edge case, last element
print(f"Index of {num} is ", binary_search(numbers, num))
num = 13
print(f"Index of {num} is ", binary_search(numbers, num))
num = -221
print(f"Index of {num} is ", binary_search(numbers, num))
num = 0
print(f"Index of {num} is ", binary_search(numbers, num))
num = -10
print(f"Index of {num} is ", binary_search(numbers, num))












