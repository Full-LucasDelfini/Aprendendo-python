valores = []
pares = []
impares = []
while True:
    num = int(input('Digite um número: '))
    valores.append(num)
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    while resp not in 'SN' or resp == '':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
print('-='*15)
for v in valores:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'A lista de valores digitadas foi respectivamente: {sorted(valores)}')
print(f'A lista de números pares foi respectivamente: {sorted(pares)}')
print(f'A lista de números ímpares foi respectivamente: {sorted(impares)}')
