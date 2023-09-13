"""
Gerando a sequência de Fibonacci
A tarefa é criar um programa que gere a sequência de Fibonacci até um determinado número n. 
Sua função deve receber um número inteiro n como entrada e imprimir a sequência de Fibonacci até o enésimo termo, 
com cada termo separado por um espaço. Por exemplo, para n = 5, a saída deve ser "0 1 1 2 3". 
Note que a sequência deve ser exibida em uma única linha e não deve haver espaço após o último número.
"""

def fibo(num):
    arr = [1,1]
    aux = num - 1
    for i in range(1,aux):
        next = arr[i-1] + arr[i]
        arr.append(next)
    #print(arr)
    
    for j in (arr):
        if arr.index(j) != (len(arr) -1):
            print(j, end= " ")
        else:
            print(j)
fibo(3)
fibo(4)
fibo(5)
fibo(6)
fibo(100)