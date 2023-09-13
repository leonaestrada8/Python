def palindromo(palavra):
    if len(palavra) < 3:
        return '?'
    invertida = palavra[::-1]
    if palavra == invertida:
        return 'PALINDROMO'
    return 'N'

palavra = "anilina"
code=palindromo(palavra)
print(f"{palavra}: {code}")
palavra = "ZaphoddohpaZ"
code=palindromo(palavra)
print(f"{palavra}: {code}")
palavra = "Marvin"
code=palindromo(palavra)
print(f"{palavra}: {code}")
palavra = "42"
code=palindromo(palavra)
print(f"{palavra}: {code}")

