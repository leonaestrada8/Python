def insertionSort(arr):
    for i in range(1, len(arr)):
        j=i
        while j > 0 and arr[j] < arr[j-1]:
            [arr[j] , arr[j-1]] = [arr[j-1] , arr[j]]
            j -= 1
    return arr

arr = [5, 1, 8, 7, 3, 4, 10, 9, 6]
print(arr)
insertionSort(arr)
print(arr)