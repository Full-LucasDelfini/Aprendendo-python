from random import randint
num = int(input('Digite qual número você acha ser o escolhido: '))
escolha = randint(1,5)
print(f'O número escolhido foi {escolha} ')
if num == escolha:
    print('Parábens! Você ganhou!')
else:
    print('Você perdeu, PATO!')