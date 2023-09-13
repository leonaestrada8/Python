def fibo_rec(n):
    if n <= 1:
        return n
    else:
        return fibo_rec(n - 1) + fibo_rec(n - 2)

n = 10
result = fibo_rec(n)
print(f"O {n}th numero da serie de Fibonacci eh {result}")  

