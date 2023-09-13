def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Encontrar o índice do elemento mínimo na parte não ordenada
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Trocar o elemento mínimo encontrado com o primeiro elemento
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

arr = [9,8,7,4,5,6,3,2,1]
print("Array original:", arr)
sorted_arr = selection_sort(arr)
print("Array ordenado:", sorted_arr)
