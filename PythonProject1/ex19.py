from random import choice
n1 = str(input('Qual o primeiro nome?'))
n2 = str(input('Qual o segundo nome?'))
n3 = str(input('Quais o terceiro nome?'))
n4 = str(input('Quais o quarto nome?'))
lista = [n1,n2,n3,n4]
print(f'dentre os nomes {n1},{n2},{n3} e {n4} o vencedor foi {choice(lista)}')
