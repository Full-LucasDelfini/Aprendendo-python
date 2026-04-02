a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = a1
cont = 1
somatot = 0
while cont <= 10:
    print(f'{c}' ,end='')
    print(' =>' if cont < 10 else '.',end=' ')
    somatot += c
    c += r
    cont += 1
print(f'\nA soma total dos 10 primeiros valores da P.A é = {somatot}')