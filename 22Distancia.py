#Distancia 2.2
import math

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def calcular_distancia(a, b):
    return math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)

numero_de_pontos = int(input("Informe o número de pontos: "))
pontos = []

for i in range(numero_de_pontos):
    x = float(input(f"Informe a coordenada X do ponto {i + 1}: "))
    y = float(input(f"Informe a coordenada Y do ponto {i + 1}: "))
    pontos.append(Ponto(x, y))

distancia_total = 0
for i in range(len(pontos) - 1):
    distancia = calcular_distancia(pontos[i], pontos[i + 1])
    print(f"Distância do ponto {i + 1} ao ponto {i + 2}: {distancia}")
    distancia_total += distancia

print(f"Distância total percorrida: {distancia_total}")
