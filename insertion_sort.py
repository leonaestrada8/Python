def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i
        while j > 0 and numbers[j] < numbers[j - 1]:
            numbers[j], numbers[j - 1] = numbers[j- 1], numbers[j]
            j -= 1
    return arr

numbers = [42, 13, 69, 5, 1, 8, 7, 3, 4, 10, 9,]
insertion_sort(numbers)
print(numbers)

