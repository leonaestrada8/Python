def mdc(a, b): # MANEIRA ALTERNATIVA DE CALCULAR MDC (ALGORITMO DE EUCLIDES):
    while b != 0:
        a, b = b, a % b
    return a

def mmc(a, b):
    return a * b // mdc(a, b)

numero1 = 12
numero2 = 18

resultado = mmc(numero1, numero2)
print(f"O MMC de {numero1} e {numero2} eh {resultado}")

