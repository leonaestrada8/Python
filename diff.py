"""
Dada uma matriz quadrada, calcule a diferença absoluta entre as somas de suas diagonais. 
 
Por exemplo, a matriz quadrada é mostrada abaixo: 
 
1 2 3 
4 5 6 
9 8 9 
 
A diagonal da esquerda para a direita = 1 + 5 + 9 = 15 . A diagonal da direita para a esquerda = 3 + 5 + 9 = 17 . Sua diferença absoluta é |15 - 17| = 2.

"""

def diff(matrix):
    d1 = d2 = 0
    for i in range (len(matrix) -1):
        d1 = d1 + matrix[i][i]
        d2 = d2 + matrix[i][len(matrix) -i -1]
    
    diff = abs(d1 - d2)
    print(f"diferenca absoluta de diagonais: {diff}")


matrix= [[1, 2, 3], 
      [4, 5, 6], 
      [9, 8, 9]] 

diff(matrix)