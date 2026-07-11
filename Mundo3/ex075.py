numeros = ()
for n in range(1, 5):
    num = int(input(f'Digite o {n}° valor: '))
    while num < 0:
        num = int(input('Digite um número válido, por favor: '))
    numeros += (num,)
print(f'Os valores digitados foram: {numeros}')
print(f'O número nove foi digitado {numeros.count(9)} vez(es)')
if 3 in numeros:
    posicao = numeros.index(3) + 1
    print(f'O valor 3 apareceu na {posicao}ª posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')