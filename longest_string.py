

def solution(inputArray):
    tamanhos = [len(item) for item in inputArray]
    max_value = max(tamanhos)
    return (item for item in inputArray if len(item) == max_value)


inputArray = ["aba", "aa", "ad", "vcd", "aba"]
print(list(solution(inputArray)))