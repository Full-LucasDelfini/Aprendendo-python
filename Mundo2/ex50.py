from time import sleep
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}° número: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print('INTERPRETANDO...')
sleep(1)
print(f'Você informou {cont} número(s) PARES e a soma é {soma}!')
