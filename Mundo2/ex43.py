from time import sleep
nome = str(input('Olá, Como você se chama? ')).strip().capitalize()
altura = float(input(f'Qual a sua altura, {nome}? '))
peso = float(input(f'Qual é o seu peso, {nome}? '))
IMC = peso / (altura ** 2)
azul = '\033[4;34m'
vermelho = '\033[1;31m'
verde = '\033[32m'
amarelo = '\033[33m'
amarelo_moderado = '\033[1;33m'
limpa = '\033[m'
print(f'{azul} CALCULANDO...{limpa}')
sleep(1.5)
if IMC < 18.5:
    print(f'{amarelo_moderado} Cuidado! Você está abaixo do peso {nome}!{limpa}')
elif IMC >= 18.5 and IMC <= 24.9:
    print(f'{verde} Parábens, {nome}! Você está no peso ideal!{limpa}')
elif IMC >= 25 and IMC <= 29.9:
    print(f'{amarelo}Você está com um leve sobrepeso {nome}!{limpa}')
elif IMC >= 30 and IMC <= 40:
    print(f'{amarelo_moderado} Você está no estágio obeso, {nome}!{limpa}')
else:
    print(f'{vermelho} CUIDADO! Você está no estágio de OBESIDADE MÓRBIDA, {nome}!{limpa}')
