from time import sleep
nome_maisvelho = ''
soma = 0
media = 0
idade_maior = 0
total_mulhermenor = 0
for c in range(1,5):
    nome = str(input(f'Digite o nome da {c}° pessoa: ')).strip()
    idade = int(input(f'Digite a idade da {c}° pessoa: '))
    genero = str(input(f'Digite o genero da {c}° pessoa M ou F: ')).strip().upper()
    soma += idade
    if c == 1 and genero == 'M':
        nome_maisvelho = nome
        idade_maior = idade
    if idade > idade_maior and genero == 'M':
        idade_maior = idade
        nome_maisvelho = nome
    if idade < 20 and genero == 'F':
        total_mulhermenor += 1
media = soma / 4
sleep(0.8)
print('-='*65)
print('INTERPRETANDO AS INFORMAÇÕES E CALCULANDO...')
sleep(0.8)
print('-='*65)
sleep(1.2)
print(f'O nome do homem mais velho é {nome_maisvelho}')
print(f'O total de mulheres menores de 20 anos é {total_mulhermenor}')
print(f'A média de idade do grupo é {media}')