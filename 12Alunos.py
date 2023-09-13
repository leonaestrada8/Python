#Alunos 1.2

def calcular_media(notas):
    return sum(notas) / len(notas)

def calcular_mediana(notas):
    notas_ordenadas = sorted(notas)
    meio = len(notas) // 2
    if len(notas) % 2 == 0:
        return (notas_ordenadas[meio - 1] + notas_ordenadas[meio]) / 2
    else:
        return notas_ordenadas[meio]

def calcular_desvio_padrao(notas, media):
    soma_das_diferencas_quadradas = sum((x - media) ** 2 for x in notas)
    variancia = soma_das_diferencas_quadradas / len(notas)
    return variancia ** 0.5

def estatisticas_turma():
    notas = [float(input("Insira a nota do aluno: ")) for _ in range(int(input("Insira o número de alunos na turma: ")))]

    media = calcular_media(notas)
    mediana = calcular_mediana(notas)
    desvio_padrao = calcular_desvio_padrao(notas, media)

    print(f"Média da turma: {media:.2f}")
    print(f"Mediana da turma: {mediana:.2f}")
    print(f"Desvio Padrão da turma: {desvio_padrao:.2f}")

#if __name__ == "__main__":
estatisticas_turma()
