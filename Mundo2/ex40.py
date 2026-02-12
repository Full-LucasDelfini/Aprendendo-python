from time import sleep
nome = str(input('Olá, estudante! Qual o seu nome? ')).strip()
n1 = float(input(f'Qual a sua primeira nota, {nome}? '))
n2 = float(input(f'Qual a sua segunda nota?, {nome}? '))
media = (n1 + n2) / 2
vermelho = '\033[1;31m'
amarelo = '\033[1;33m'
verde = '\033[1;32m'
limpa = '\033[m'
print('CALCULANDO...')
sleep(1.4)
if (n1 > 10 or n2 > 10) or (n1 < 0 or n2 < 0):
    print(f'{vermelho} ERRO! as notas não podem ser maior que 10 ou menor que 0! {limpa}')
elif media < 5:
    print(f'{vermelho} Infelizmente você foi reprovado, {nome}! Sua média final foi {media}{limpa}')
elif media >= 5 and media <= 6.9:
    print(f'{amarelo} Você está de recuperação, {nome}! Sua média atual é {media} {limpa}.')
else:
    print(f'{verde} Parabéns, {nome}! Você foi aprovado com a média de {media} {limpa}!')
