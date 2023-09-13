def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Exemplo de uso
arr = [5,1,8,7,3,4,10,9,2,6]
bubble_sort(arr)
print("Array ordenado:", arr)
