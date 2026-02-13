from datetime import date
nome = str(input('Olá! Para começarmos digite o seu nome: ')).strip()
ano = int(input(f'Perfeito, {nome}! Em que ano você nasceu? '))
idade = date.today().year - ano
verde = '\033[1;32m'
vermelho = '\033[1;31m'
limpa = '\033[m'
if idade <= 0:
    print(f'{vermelho} ERRO, não existe idade menor ou igual a zero!{limpa}')
elif idade <= 9:
    print(f'{verde} Parabéns, {nome}! Você pertence a categoria MIRIM.{limpa}')
elif idade > 9 and idade <= 14:
    print(f'{verde} Parabéns,{nome}! Você pertence a categoria INFANTIL.')
elif idade > 14 and idade <= 19:
    print(f'{verde} Parabéns, {nome}! Você pertence a categoria JUNIOR.{limpa}')
elif idade == 20:
    print(f'{verde} Parabéns, {nome}! Você pertence a categoria SENIOR.{limpa}')
else:
    print(f'{verde} Parabéns, {nome}! Você pertence a categoria MASTER.{limpa}')