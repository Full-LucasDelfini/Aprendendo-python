numeros = []
novo = 'S'
while True:
    num = int(input('Digite um número: '))
    if num not in numeros:
        numeros.append(num)
    else:
        print(f'O valor {num} já foi escrito, não vou adicionar repetidos!')
    novo = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if novo == 'N':
        break
print(f'A ordem dos números digitados foi: {sorted(numeros)}')