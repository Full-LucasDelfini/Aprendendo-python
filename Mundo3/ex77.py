meu_futuro = ('EU', 'SEREI', 'FUTURAMENTE', 'UM', 'DESENVOLVEDOR', 'FULL', 'STACK', 'SENIOR')
print(f'Dentre as palavras: {meu_futuro}')
for p in meu_futuro:
    print(f'\nNa palavra {p:.<15} possui as seguintes vogais:', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')