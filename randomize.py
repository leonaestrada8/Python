import random

def randomize(arr):
    n = len(arr)
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i) # índice aleatório no intervalo [0, i]
        arr[i], arr[j] = arr[j], arr[i]  
    return arr

nomes = ["VogonCode", "InfiniteImprobabilitySource", "DontPanic_Code", "MarvinScripts", "FordPrefect"]
result = randomize(nomes)
print(result) 
numbers = [42,69,66,77,88,99999,756,33,45,13]
result = randomize(numbers)
print(result) 

