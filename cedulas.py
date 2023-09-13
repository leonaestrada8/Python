
"""
100, 50, 20, 10, 5, 2, 1

"""


def cedulas (num):
    print(f"{num} reais:")
    arr = [100, 50, 20 , 10, 5 , 2]
    aux0 = 0
    for i in range(len(arr)):
        if aux0 == 0:
            aux1 = num // arr[i]
            aux0 = num % arr[i]
        else:
            aux1 = aux0 // arr[i]
            aux0 = aux0 % arr[i]
        if aux1 > 0:
            print(f"{aux1} ..................notas de {arr[i]}")
        elif (i == len(arr)-1) and aux0 > 0:
            print(f"{aux0} ..................notas de 1")
    
num = 576
cedulas(num)