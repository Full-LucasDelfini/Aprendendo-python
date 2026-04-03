a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
termo = a1
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} => ', end='')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais você quer mostrar? '))
print(f'\nProgressão finalizada com {total} termos mostrados.')