"""
For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
solution(a) = [-1, 150, 160, 170, -1, -1, 180, 190].    
    """
    
def sort_height(a):
    b = []
    for j in range (len(a)):
        b.append(999)
    c = []
    for i in range (len(a)):
        print(i)
        if a[i] == -1:
            b[i] = a[i]
        else:
            c.append(a[i])
    c.sort()
    aux=0
    for k in range(len(a)):
        if b[k] == 999:
            b[k] = c[aux]
            aux += 1
    return b



a = [-1, 150, 190, 170, -1, -1, 160, 180]

    
print(sort_height(a))