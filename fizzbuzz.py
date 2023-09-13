def fizzbuzz(inicio, fim):
    resultado = []
    for i in range(inicio, fim + 1):
        if i % 3 == 0 and i % 5 == 0:
            resultado.append("FizzBuzz")
        elif i % 3 == 0:
            resultado.append("Fizz")
        elif i % 5 == 0:
            resultado.append("Buzz")
        else:
            resultado.append(i)
    return resultado

inicio = 1
fim = 15
resultados = fizzbuzz(inicio, fim)
print(resultados)
