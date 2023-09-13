'''
Suponha que você tenha uma haste de comprimento n e uma tabela de preços p[i] para hastes de comprimento i = 1, 2, ..., n. 
Determine a maneira de cortar a haste em peças de comprimentos integrais para maximizar o lucro de venda das peças. 
Note que se o preço de corte for maior que o comprimento da haste, pode ser mais rentável não cortar a haste em alguns casos.
'''


def cut_rod(p, n):
    # Inicializa uma tabela de valores com zeros
    # val[i] é o melhor valor alcançável para uma haste de comprimento i
    val = [0 for _ in range(n + 1)]
    print(f"val: {val}")
    
    # Constroi a tabela val de maneira bottom-up
    # A solução para cada subproblema depende de soluções anteriores
    for i in range(1, n + 1):
        max_val = float('-inf')
        for j in range(i):
            max_val = max(max_val, p[j] + val[i - j - 1])
        val[i] = max_val
        print(f"val[i] = {max_val}")
        print(f"-----------------------------------val: {val}")
    
    return val[n]

# Exemplo de entrada
p = [1, 5, 8, 9, 10, 17, 17, 20]
n = len(p)

# Saída: 22
print(cut_rod(p, n))
