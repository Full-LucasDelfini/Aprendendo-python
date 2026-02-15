from random import choice
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = choice(itens)
preto = '\033[1;30;107m'
azul = '\033[4;34m'
vermelho = '\033[4;31m'
amarelo = '\033[4;33m'
limpa = '\033[m'
nome = str(input('Olá! Como você se chama? ')).strip().capitalize()
print(f'''{preto} Temos 3 opções: {limpa} 
{azul} [ 1 ] Pedra {limpa}
{amarelo} [ 2 ] Papel {limpa}
{vermelho} [ 3 ] Tesoura {limpa}''')
opcao = int(input(f'Qual a sua opção, {nome}? '))
jogador = itens[opcao - 1]
print('JO...')
sleep(0.7)
print('KEN...')
sleep(0.7)
print('PÔ!!!')
sleep(0.5)
if jogador == computador:
    print(f'{amarelo}EMPATE! O computador também escolheu \"{computador}\", {nome}! {limpa}')
elif(jogador == 'Pedra' and computador == 'Tesoura') or \
    (jogador == 'Tesoura' and computador == 'Papel') or \
    (jogador == 'Papel' and computador == 'Pedra'):
    print(f'{azul} PARÁBENS! O computador escolheu \"{computador}\", VOCÊ GANHOU, {nome}! {limpa}')
else:
    print(f'{vermelho}HAHA! Você perdeu, o computador escolheu \"{computador}\", {nome}! {limpa}')