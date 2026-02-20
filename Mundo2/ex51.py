from time import sleep
n1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
print('EXECUTANDO...')
sleep(1)
decimo = n1 + (9 * r)
for c in range(n1, decimo + r, r):
    print(f'{c}', end=' => ')
print('FIM!')
