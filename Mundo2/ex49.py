from time import sleep
num = int(input('Digite um número para executarmos a sua tabuada: '))
print('\033[4;31m CALCULANDO...')
sleep(1)
for c in range(1, 11):
    print(f'{num} x {c} = {num * c}')