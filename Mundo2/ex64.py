soma = cont = 0
num = int(input('Digite um número inteiro [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite outro número inteiro [999 para parar]: '))
if cont > 1:
    print(f'Você digitou {cont} números e sua soma total foi : {soma}.')
elif cont == 1:
    print(f'Você digitou apenas um número, portanto a soma será ele mesmo : {soma}.')
else:
    print('Você não digitou nenhum número válido.')