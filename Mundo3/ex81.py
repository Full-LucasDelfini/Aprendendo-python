lista_numeros = []
while True:
    num = int(input('Digite um número: '))
    lista_numeros.append(num)
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=-='*30)
print(f'Ao todo foram digitados {len(lista_numeros)} números!')
lista_numeros.sort(reverse=True)
print(f'A lista de valores de forma decrescente é {lista_numeros}')
if 5 in lista_numeros:
    print('O número 5 pertence a lista de números!')
else:
    print('O número 5 não pertence a lista!')
