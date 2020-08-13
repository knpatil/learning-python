# add numbers from a given list

def list_sum(numbers):
    the_sum = 0
    for i in numbers:  # iterative, iterations (repetations)
        the_sum = the_sum + i
    return the_sum


def list_sum_recursive(numbers):
    if len(numbers) == 1:  # base case
        return numbers[0]
    else:  # recursive case
        return numbers[0] + list_sum_recursive(numbers[1:])


# Three laws of recursion
# 1. recursive algorithm must have a base case
# 2. recursive algorithm must change its state and move towards the base case
# 3. recursive algorithm must call itself, recursively

# nums = [1, 3, 5, 7, 9]
# print("Sum = ", list_sum_recursive(nums))

# 1 1 2 3 5 8 13
# fibonacci series
# memoization/caching -- dynamic programming
def fibonacci(n, cache):
    """
    Program to display the Fibonacci sequence up to n-th term
    """
    if n <= 0:
        raise ValueError("Invalid Input!")

    # check if this fib is already calculated
    if n in cache:
        print(f"\nReturning fib from memory for {n}")
        return cache[n]

    print(f"Computing fib for {n}")
    if n == 1 or n == 2:
        fib = 1
    else:
        fib = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)

    cache[n] = fib
    return fib


cache = dict()
for i in range(1, 100):
    print(fibonacci(i, cache))

print("\n\n\n")
print(cache)


# 3 * 4 = 3 + 3 + 3 + 3 = 12
# 34 * 23 =