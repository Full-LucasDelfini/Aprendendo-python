num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
     [ 1 ] Opção para BINÁRIO
     [ 2 ] Opção para OCTAL
     [ 3 ] Opção para HEXADECIMAL''')
opcao = int(input('Qual a opção desejada acima? '))
if opcao == 1:
    print(f'A conversão de {num} para BINÁRIO é: {bin(num)[:2]}')
elif opcao == 2:
    print(f'A conversão de {num} para OCTAL é: {oct(num)[:2]}')
elif opcao == 3:
    print(f'A conversão de {num} para HEXADECIMAL é: {hex(num)[:2]}')
else:
    print(f'{num} é um opção inválida!')
