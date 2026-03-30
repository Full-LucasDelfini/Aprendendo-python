from time import sleep
vermelho = '\033[0;31m'
verde = '\033[0;32m'
amarelo = '\033[33m'
roxo = '\033[35m'
azul = '\033[34m'
limpa = '\033[m'
opcao = 0
print(f'{amarelo}*{azul}~{amarelo}*{azul}~{limpa}' * 30)
print(f'INTERPRETADOR DE NÚMEROS E SUAS OPERAÇÕES')
print(f'{amarelo}*{azul}~{amarelo}*{azul}~{limpa}' * 30)
sleep(0.7)
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
sleep(0.2)
print(f'{amarelo}*{azul}~{amarelo}*{azul}~{limpa}' * 30)
while opcao != 6:
    print(f'''{verde}[ 1 ] SOMAR {limpa}
{azul}[ 2 ] MULTIPLICAR {limpa}
{amarelo}[ 3 ] MAIOR E MENOR {limpa}
{roxo}[ 4 ] DIVISÃO {limpa}
[ 5 ] NOVOS NUMEROS
{vermelho}[ 6 ] SAIR DO PROGRAMA {limpa}''')
    print(f'{amarelo}*{azul}~{amarelo}*{azul}~{limpa}' * 30)
    opcao = int(input('Digite sua opção: '))
    print(f'\033[1;4;36m INTERPRETANDO... {limpa}')
    sleep(1)
    if opcao == 1:
        soma = n1 + n2
        print(f'{verde}A soma entre {n1:.0f} e {n2} é: \033[4;32m {n1:.0f} + {n2:.0f} = {soma:.0f}{limpa}')
        print(f'{amarelo}*{azul}~{amarelo}*{azul}~{limpa}' * 30)
        sleep(1.7)
    elif opcao == 2:
        multiplicar = n1 * n2
        print(f'A multiplicação entre {n1:.0f} e {n2:.0f} é: {n1:.0f} X {n2:.0f} = {azul}{multiplicar:.0f}{limpa}')
        print(f'{amarelo}*{azul}~{amarelo}*{azul}~{limpa}' * 30)
        sleep(1.7)
    elif opcao == 3:
        if n1 > n2:
            print(f'Maior = {n1}')
            print(f'Menor = {n2}')
            print(f'{amarelo}*{azul}~{amarelo}*{azul}~{limpa}' * 30)
            sleep(0.7)
        else:
            print(f'Maior = {n2}')
            print(f'Menor = {n1}')
            print(f'{amarelo}*{azul}~{amarelo}*{azul}~{limpa}' * 30)
            sleep(1.7)
    elif opcao == 4:
        if n2 != 0:
            divisao = n1 / n2
            print(f'A divisão entre {n1:.0f} e {n2:.0f} é: {divisao:.2f}')
        else:
            print(f'{vermelho}ERRO: Não é possível dividir por zero!{limpa}')
        print(f'{amarelo}*{azul}~{amarelo}*{azul}~{limpa}' * 30)
        sleep(1.7)
    elif opcao == 5:
        print('Informe os números novamente:')
        n1 = float(input('Primeiro valor: '))
        n2 = float(input('Segundo valor: '))
        print(f'{amarelo}*{azul}~{amarelo}*{azul}~{limpa}' * 30)
        sleep(1.7)
    elif opcao == 6:
        print(f'{vermelho} ENCERRANDO...{limpa}')
        sleep(1.0)
    else:
        print(f'{vermelho} Opcão inválida, Digite novamente!{limpa}')
print(f'\033[1;4;36m Obrigado por participar, sistema encerrado!{limpa}')