from time import sleep
from random import randint
def sorteia (lista):
    print(f'Sorteando 5 valores da lista: ', end='')
    for num in range(0,5):
        n = randint(0,10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.5)

def somapar(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    print(f'\nSomando os valores para da lista {lista} temos {soma}')

numeros = list()
sorteia(numeros)
somapar(numeros)