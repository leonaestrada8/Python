def mdc(a, b):
    menor_numero = min(a, b)
    for divisor in range(menor_numero, 0, -1):
        if a % divisor == 0 and b % divisor == 0:
            return divisor

numero1 = 56
numero2 = 48

resultado = mdc(numero1, numero2)

print(f"O maior divisor comum entre {numero1} e {numero2} eh {resultado}")  

