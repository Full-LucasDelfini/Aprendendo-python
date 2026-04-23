valores = []
for v in range(0,5):
    num = int(input(f'Digite o valor para a posição {v}: '))
    valores += num,
maior = max(valores)
menor = min(valores)
print(f'o maior valor foi {maior} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}... ', end='')
print(f'\nO menor valor foi {menor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}... ', end='')

