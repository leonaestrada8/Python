def segundoMaior(arr):
    arr_aux = list(arr)
    arr_aux.sort()
    for i in range(len(arr_aux) - 1, 0, -1):  # Iterate backwards to avoid skipping elements when removing
        print (f"{arr[i]} == {arr[i-1]}")
        if arr_aux[i] == arr_aux[i - 1]:
            arr_aux.remove(arr_aux[i])
    print(arr_aux)
    print(arr_aux[-2])

arr = [2, 3, 6, 6, 5]
segundoMaior(arr)



            

        