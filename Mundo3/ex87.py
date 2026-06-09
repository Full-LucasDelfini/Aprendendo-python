somapares = somacolu3 = maiorl2 = 0
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha},{coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            somapares += matriz[linha][coluna]
        if coluna == 2:
            somacolu3 += matriz[linha][2]
        if linha == 1:
            if coluna == 0:
                maiorl2 = matriz[linha][coluna]
            elif matriz[linha][coluna] > maiorl2:
                maiorl2 = matriz[linha][coluna]
print(f'A soma dos valores pares foi: {somapares}')
print(f'A soma dos valores da terceira coluna foi: {somacolu3}')
print(f'O maior número digitado na segunda linha foi: {maiorl2}')
