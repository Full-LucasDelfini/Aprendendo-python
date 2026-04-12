from random import randint
from time import sleep
cont = 0
print('-=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR!')
print('-=-'*20)
while True:
    computador = randint(0, 10)
    num = int(input('Qual valor você escolheu? '))
    classe = str(input('Você escolhe par ou impar? [P/I] ')).strip().upper()[0]
    soma = num + computador
    if classe == 'P':
        if soma % 2 == 0:
            print(f'Parabéns, você ganhou! O computador escolheu {computador} e você {num}, a soma de {soma} é PAR.')
            cont += 1
            print('-=-'*20)
            print('Vamos jogar novamente...')
            sleep(2)
        else:
            print(f'O computador escolheu {computador} e você {num}, a soma de {soma} é ÍMPAR.')
            print(f'GAME OVER! Você venceu {cont} vezes antes de perder.')
            break
    else:
        if soma % 2 != 0:
            print(f'Parabéns, você ganhou! O computador escolheu {computador} e você {num}, a soma de {soma} é IMPAR.')
            cont += 1
            print('-=-' * 20)
            print('Vamos jogar novamente...')
            sleep(2)
        else:
            print(f'O computador escolheu {computador} e você {num} a soma de {soma} é PAR')
            print(f'GAME OVER! Você venceu {cont} vezes antes de perder.')
            break

