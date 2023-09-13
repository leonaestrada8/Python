"""
Dada um ARRAY de números inteiros, calcule as proporções de seus elementos que são positivos, negativos e zero. Imprima o valor decimal de cada fração em uma nova linha com 6 casas após o decimal.

Exemplo:
ARR = [1,1,0.-1,-1]
Existem n=5 elementos, dois positivos, dois negativos e um zero. Suas razões são:

[OUTPUT DO CÓDIGO]:
POSITIVO: 0,400000
NEGATIVO: 0,400000
ZEROS: 0,200000

"""

def plusMinus(arr):
    pos = neg = zero = 0
    for num in arr:
        if num > 0:
            pos += 1
        elif num == 0:
            zero += 1
        else:
            neg += 1
    qtd = len(arr)
    print(f"POSITIVOs: {pos/qtd:.6f}")
    print(f"NEGATIVOs: {neg/qtd:.6f}")
    print(f"ZEROs: {zero/qtd:.6f}")
    
arr = [1,1,0,-1,-1]
plusMinus(arr)
            