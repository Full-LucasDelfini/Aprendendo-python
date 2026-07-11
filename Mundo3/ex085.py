numeros = [[],[]]  # (pares na pos 0, impares na pos 1)
valor = 0
for c in range(1, 8):
    valor = int(input(F'Digite o {c}° valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
print('-='*30)
numeros[0].sort()
numeros[1].sort()
print(f'Os valores pares digitados foram {numeros[0]}')
print(f'Os valores impares digitados foram {numeros[1]}')