def bubble_sort(arr):

    print(f"Before Sorting: {arr}")

    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
        print(arr)

    print(f"After Sorting: {arr}")


numbers = [8, 1, 5, 0, -1]
bubble_sort(numbers)

