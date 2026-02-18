soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
        #print(f'{c} ', end='')
print(f'A soma de todos os {cont} valores é {soma}')
#este ex calcula todos os números múltiplos de 3 no intervalo de 0 à 500.
