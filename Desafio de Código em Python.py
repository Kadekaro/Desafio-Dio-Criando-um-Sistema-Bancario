"""
Desafio 2/3:

month = input()
months_dict = {
    '1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May', '6': 'June',
    '7': 'July', '8': 'August', '9': 'September', '10': 'October', '11': 'November', '12': 'December'
}

for i, j in enumerate(months_dict):   Pode-se usar esse método usando o enumerate, ou o de baixo usando somente o if ^^
    if j == month:
        print(months_dict[j])


if month in months_dict.keys():
    print(months_dict[month])
"""


# Desafio 3/3:

def encaixa(A, B):
    if len(A) < len(B):
        return "nao encaixa"

    if A[-len(B):] == B:
        return "encaixa"
    else:
        return "nao encaixa"


N = int(input())

i = 0
while i < N:
    A, B = input().split()
    resultado = encaixa(A, B)
    print(resultado)
    i += 1
