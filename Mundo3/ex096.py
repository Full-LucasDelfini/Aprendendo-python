def area (l, c):
    result = l * c
    print(f'A área do terreno {l}x{c} é: {result}m²')


def titulo(txt):
    print('-' * 30)
    print(f'{txt:^30}')
    print('-' * 30)


titulo('   CONTROLE DE TERRENOS   ')
#PROGRAMA PRINCIPAL
a = int(input('Comprimento (m): '))
b = int(input('Largura (m): '))
area(a,b)