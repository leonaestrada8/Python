def busca_linear(lista, elemento_procurado):
    for indice, elemento in enumerate(lista):
        if elemento == elemento_procurado:
            return indice  
    return -1  

lista = [34, 56, 78, 12, 44, 89, 23, 42, 13]
elemento_procurado = 42

indice_encontrado = busca_linear(lista, elemento_procurado)

if indice_encontrado != -1:
    print(f"Elemento {elemento_procurado} encontrado na posicao {indice_encontrado}.")
else:
    print(f"Elemento {elemento_procurado} nao encontrado na lista.")
    
    

