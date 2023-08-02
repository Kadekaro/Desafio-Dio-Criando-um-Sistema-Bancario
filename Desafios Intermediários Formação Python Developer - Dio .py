# Desafio 1 / 3 - Dragão:

# C = int(input())
# for i in range(C):
#     N = int(input())
#     if N > 8000:
#         print('Mais de 8000!')
#     else:
#         print("Inseto!")


# Desafio 2/3 :

# T = int(input())
# for i in range(T):
#     N, K = map(int, input().split())
#     if K >= 1 and N <= 10000:
#         print(f'{(N//K) + (N % K)}')


# Desafio 3/3:

a = input()
b = input()
c = input()

if a == 'vertebrado' and b == 'ave' and c == 'carnivoro':
    print(f'aguia')
elif a == 'vertebrado' and b == 'ave' and c == 'onivoro':
    print(f'pomba')
elif a == 'vertebrado' and b == 'mamifero' and c == 'onivoro':
    print(f'homem')
elif a == 'vertebrado' and b == 'mamifero' and c == 'herbivoro':
    print(f'vaca')

if a == 'invertebrado' and b == 'inseto' and c == 'hematofago':
    print(f'pulga')
elif a == 'invertebrado' and b == 'inseto' and c == 'herbivoro':
    print(f'lagarta')
elif a == 'invertebrado' and b == 'anelideo' and c == 'hematofago':
    print(f'sanguessuga')
elif a == 'invertebrado' and b == 'anelideo' and c == 'onivoro':
    print(f'minhoca')
