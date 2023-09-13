def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

numero = 5
print(f"O fatorial de {numero} eh {fatorial(numero)}")  # Saída: O fatorial de 5 é 120
