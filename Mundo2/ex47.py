from time import sleep
vermelho = '\033[4;31m'
azul = '\033[4;34m'
limpa = '\033[m'
print(f'{azul} Dentre a lista de 0 à 50, os números pares são: {limpa}')
for c in range(0, 52, 2):
    sleep(0.5)
    print(f'{azul} {c} {limpa}')
print(f'{vermelho} FIM!!! {limpa}')