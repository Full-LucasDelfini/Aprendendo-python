from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0

for c in range(1, 8):
    ano = int(input(f'Digite o ano em que a {c}° pessoa nasceu: '))
    idade = atual - ano

    if idade >= 18:
        totalmaior += 1
    else:
        totalmenor += 1

print(f'Ao todo tivemos {totalmaior} pessoa(s) maior(es) de idade! ',end='')
print(f'E ao todo tivemos {totalmenor} pessoa(s) menor(es) de idade! ')