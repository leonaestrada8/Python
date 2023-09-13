"""
    Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

For n = 1230, the output should be
solution(n) = true;
For n = 239017, the output should be
solution(n) = false.
    """


def lottery(n):
    lista_n = list(str(n))
    print(lista_n)
    half = len(lista_n)//2
    first = sum(int(number) for number in lista_n if number in lista_n[half:])
    last = sum(int(number) for number in lista_n if number in lista_n[:half])
    return first == last

n = 1230
print(lottery(n))
