from random import randint
from time import sleep
cont = []
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'Sorteando {jogos} jogos!')
print('-='*30)
sleep(1)
for j in range(jogos):
    while len(cont) < 6:
        numero = randint(1,60)
        if numero not in cont:
            cont.append(numero)
    cont.sort()
    print(f'jogo {j + 1}: {cont}')
    sleep(1)
    cont.clear()