from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10), randint(1, 10))
for n in numeros:
    print(n, end=' ')
print(f'\nO maior número sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
