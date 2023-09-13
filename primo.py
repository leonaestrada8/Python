def numeros_primos_no_intervalo(inicio, fim):
    primos = []
    for num in range(inicio, fim + 1):
        if num > 1:
            isPrime = True
            for i in range(2, num):  
                if (num % i) == 0:
                    isPrime = False
                    break
            if isPrime:
                primos.append(num)
    return primos

inicio = 0
fim = 42
primos = numeros_primos_no_intervalo(inicio, fim)
print(f"Numeros primos no intervalo de {inicio} a {fim}: {primos}")

