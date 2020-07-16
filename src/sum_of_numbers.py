
import time

def sum_of_numbers(n): # input is n
    """calculate the sum of n numbers"""
    start_time = time.time()

    the_sum = 0  # 1 time
    for i in range(0, n+1):
        the_sum = the_sum + i  # n times

    end_time = time.time()

    return the_sum, end_time - start_time


# what is the time complexity of the above function
# it is O(n)
# it is going to take time in order of magnitude of n

# O(log n)

# O(   )

# worst case: O(n) --> Big-O notation

arr = [4, 2, 5, 1, 3, 7, 3432, 434, 53, 132344, 424, 4, 44, 44]

# find some element in this array, return index
def find_element(nums, element):
    for i in range(0, len(nums)):
        if element == nums[i]:
            return i
    return -1  # not found

# n  <- generic term , it means the size of the problem

print(find_element(arr, 3))
print(find_element(arr, 4)) # 1 operation O(1) -> constant time
print(find_element(arr, 1)) # 1 operation O(4) -> constant time





# T <- time it takes to solve a problem
# T(n) <- time it takes to solve a problem of size n
# T(n) = 1 + n  <--- actual time takes, dominant factor
#
# order of magnitude -> Big-O notation (O -> order)
# O(f(n)) -> O(n)
# O(f(n)) = O(n)











# total steps = n + 1 operations
# T(n) = n + 1 # Order of magnitude of input




# def sum_of_numbers_2(n):
#     start_time = time.time()
#     x = 0 # 1
#     for y in range(1, n+1):
#         z = y  # n - 1
#         x = x + z  # n -1
#     end_time = time.time()
#     return x, end_time - start_time

# 1 + n - 1 + n - 1 = 2n - 1 = 2n
# T(n) = 2n - 1
# O(n) = nˆ2  => nˆ2

# for n in (10_000, 1_00_000, 1_000_000, 10_000_000, 100_000_000):
#     print(sum_of_numbers(n))

#
# measure it in terms of input size -> n input size
# performance will change
# T(n) =
# Order of magnitude of input => size of input
# Big-O Notation T(n) -> O(n) = n + 1 <- time complexity  for sum_of_numbers
# O(n) = n   <- time complexity  for sum_of_numbers_2
# O of n , Big O of n, time complexity

# nˆ2  :  4 64  10000   100000000  <- n becomes really large
# 4n   :  8 32          40000

#
# Big-O Notation
#