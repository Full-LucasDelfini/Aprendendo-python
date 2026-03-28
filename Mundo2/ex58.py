from random import randint
computador = randint(1, 10)
cont = 0
escolha = 0
while escolha != computador:
    escolha = int(input('Digite um número inteiro entre 1 e 10: '))
    cont += 1
    if escolha not in range(1, 11):
        print('Escolha invalida, tente novamente!')
    elif escolha != computador:
        print(f'Ainda não, o número escolhido não foi {escolha}! Tente novamente:')
if escolha == 1:
    print(f'Parabéns, o número escolhido foi {computador}, você acertou em sua {cont}° tentativa, Baita chute!')
else:
    print(f'Parabéns, o número escolhido foi {computador}, você acertou em sua {cont}° tentativa!')

