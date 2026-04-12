print('-' * 30)
print(f'{"LOJA SEM GARANTIA":^30}')
print('-' * 30)
totcompra = maiormil = menor_preco = cont = 0
barato = ''
while True:
    prod = str(input('Nome do produto: ')).strip().upper()
    preco = float(input('Valor do produto: R$ '))
    cont += 1
    totcompra += preco
    if preco > 1000:
        maiormil += 1
    if cont == 1 or preco < menor_preco:
        menor_preco = preco
        barato = prod
    resp = ' '
    while resp not in 'SN':
        entrada = str(input('Quer continuar? [S/N] ')).strip().upper()
        if entrada:
            resp = entrada[0]
    if resp == 'N':
        break
print(f'\n{" FIM DO PROGRAMA ":=^30}')
print(f'O total da compra foi R$ {totcompra:.2f}')
print(f'Temos {maiormil} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {barato} que custou R$ {menor_preco:.2f}')
