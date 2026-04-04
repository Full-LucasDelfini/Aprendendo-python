cont = soma = maior = menor = 0
resp = 'S'
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
media = soma / cont
print(f'Você digitou {cont} números e a soma total foi: {soma}.')
print(f'A média dentre os valores digitados foi {media:}.')
if maior == menor:
    print(f'Não houve número maior e menor, os valores digitados {maior} e {menor} são iguais')
else:
    print(f'O maior número digitado foi {maior} e o menor foi {menor}.')
print('Obrigado por participar!')