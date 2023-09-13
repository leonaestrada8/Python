def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

numbers = [42, 13, 69, 5, 99, 27, 19, 57, 71, 81, 11, 31, 8, 50, 64]
sorted_numbers = quicksort(numbers)
print("Array ordenado:", sorted_numbers)

