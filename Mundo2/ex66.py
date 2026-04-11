cont = soma = 0
while True:
    num = int(input('Digite um número inteiro [999 para parar]: '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'Você digitou {cont} valores e a soma foi {soma}')
