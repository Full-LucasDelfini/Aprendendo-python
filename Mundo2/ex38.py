from time import sleep
n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))
print('PROCESSANDO...')
sleep(1.5)
if n1 > n2:
    print(f'\033[;1;34;107m Dentre os números mencionados {n1} e {n2}, o maior é {n1}\033[m!')
elif n2 > n1:
    print(f'\033[;1;31;107m Dentre os números mencionados {n1} e {n2}, o maior é {n2}\033[m!')
else:
    print(f'\033[;1;33;107m Os números digitados {n1} e {n2} são iguais\033[m!')