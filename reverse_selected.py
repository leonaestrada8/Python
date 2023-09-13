def reverse_sel(input):
    aux1 = aux2 = -1
    lista = list(input)
    print(lista)
    lista2 = [i for i in lista if i != "(" and i != ")"]
    print(lista2)
    for j in range(len(lista)):
        if lista[j] == "(":
            aux1 = j
            for k in range(len(lista) - 1, -1, -1):
                    if lista[k] == ")":
                        aux2 = k
                        break
        break
    reverse = lista[aux1:aux2+1]
    reversed = reverse.reverse()
    print (list(reversed))
    if aux1 != -1 and aux2 != -1:
        reverse = lista[aux1 + 1:aux2]
        reverse.reverse() # Reversing in place
        lista[aux1 + 1:aux2] = reverse # Replacing the reversed content
    for l in range(aux1+1, aux2):
        if lista(l) == "(":
            aux1 = j
            for m in range(aux2, -1, -1):
                    if lista[m] == ")":
                        aux2 = m
                        break
        break
    reverse = lista[aux1:aux2+1]
    reversed = reverse.reverse()
    print (list(reversed))
    if aux1 != -1 and aux2 != -1:
        reverse = lista[aux1 + 1:aux2]
        reverse.reverse() # Reversing in place
        lista[aux1 + 1:aux2] = reverse
    return lista
            
            
    
    
""" 
    for n,i in enumerate(a):
        if i == -1:
            l.insert(n,i)
    return l
"""

input = "(bar)"
print(reverse_sel(input))
print("--------------------------")
input = "foo(bar)baz"
print(reverse_sel(input))
print("--------------------------")
input = "foo(bar)baz(blim)"
print(reverse_sel(input))
