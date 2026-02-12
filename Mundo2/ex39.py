from datetime import date
from time import sleep
nome = str(input('Digite seu nome: ')).strip()
sexo = str(input('Digite seu gênero: ')).upper().strip()
ano = int(input('Em que ano você nasceu? '))
idade = date.today().year - ano
tempo = abs(idade-18)
plural = 'ano' if tempo == 1 else 'anos'
print('PROCESSANDO...')
sleep(1.5)
if idade > 18 and sexo.upper() == 'MASCULINO':
    print(f'Já passou da hora de se alinhar, {nome}! Você deveria ter se alistado há {tempo} {plural}!')
elif idade == 18 and sexo.upper() == 'MASCULINO':
    print(f'Você está com a idade mínima para se alistar, {nome}!')
elif idade < 18 and sexo.upper() == 'MASCULINO':
    print(f'Não está no momento ainda, {nome}! Você poderá se alistar daqui {tempo} {plural}!')
elif sexo.upper() == 'FEMININO' and idade == 18:
    print(f'O seu alistamento não é obrigatório, {nome}, mas caso opte você está na idade mínima para se alistar! ')
elif sexo.upper() == 'FEMININO' and idade > 18:
    print(f'Já passou da hora de se alistar, {nome}! Você deveria ter se alistado há {tempo} {plural}!')
else:
    print(f'Não está no momento ainda {nome}! Você poderá se alistar daqui {tempo} {plural}!')