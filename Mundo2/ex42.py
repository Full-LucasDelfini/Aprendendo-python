from time import sleep
r1 = float(input('Qual a primeira reta? '))
r2 = float(input('Qual a segunda reta? '))
r3 = float(input('Qual a terceira reta? '))
vermelho = '\033[1;31m'
verde = '\033[1;32m'
amarelo = '\033[1;33m'
azul = '\033[1;34m'
limpa = '\033[m'
print('PROCESSANDO...')
sleep(1.5)
if (r1 < r2 + r3) and (r2 < r1 + r3) and (r3 < r1 + r2):
    print(f'{verde}As retas {r1}, {r2} e {r3} formam um tríangulo{limpa}',end='')
    if r1 == r2 == r3:
        print(f'{azul} EQUILÁTERO! {limpa}')
    elif (r1 == r2) or (r2 == r3) or (r3 == r1):
        print(f'{amarelo} ISÓSCELES! {limpa}')
    else:
        print(f'{vermelho} ESCALENO!{limpa}')
else:
    print(f'{vermelho} As retas {r1}, {r2} e {r3} NÃO FORMAM UM TRIANGULO! {limpa}')