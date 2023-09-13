def fibo_it(num):
    fib = [0,1]
    if (num <= 0):
        fib = []
        return fib
    if (num <= 1):
        return [fib[0]]
    elif (num == 2):
        return fib
    else:
        for i in range(num-2):
            temp = fib[i] + fib[i+1]
            fib.append(temp)
    return fib

x = 13
sequencia_fib = fibo_it(x)
print(f"SEQUENCIA FIBONNACI: {sequencia_fib}")
if (len(sequencia_fib)>0):
    print(f"Posicao {x} na sequencia fibonacci = {sequencia_fib[len(sequencia_fib) -1]}")
else:
    print(f"Numero {x} INVALIDO!")


            
        