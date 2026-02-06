dist = float(input('Qual a distância em Km: '))
if dist <= 200:
    preco1 = dist * 0.5
    print(f'Devido ao deslocamento de {dist:.2f} o valor da passagem será R$: {preco1:.2f}')
else:
    preco2 = dist * 0.45
    print(f'Devido ao deslocamento de {dist:.2f} o valor da passagem será R$: {preco2:.2f}')
