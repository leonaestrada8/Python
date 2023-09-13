def binary_search(arr, x):
    arr.sort()  # Ordenando a matriz
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        print("mid = left + (right - left) // 2")
        print(f"mid = {left} + ({right} - {left}) // 2")
        print(mid)

        # Verifique se x está presente no meio
        if arr[mid] == x:
            return mid

        # Se x for maior, ignore a metade esquerda
        elif arr[mid] < x:
            left = mid + 1

        # Se x for menor, ignore a metade direita
        else:
            right = mid - 1

    # Se não encontramos o elemento, retornamos -1
    return -1

arr = [5,6,7,3,2,1,15,10,77,88,99,42,35,21,1,12,13]
x = 13

# Chamando a função
result = binary_search(arr, x)

if result != -1:
    print(f"Elemento encontrado no indice {result}")
else:
    print("Elemento nao encontrado na matriz")
