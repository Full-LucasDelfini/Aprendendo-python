def inteiro(msg):
    valor = 0
    ok = False
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO! Digite um número válido')
        if ok:
            break
    return valor
n = inteiro('Digite um número inteiro: ')
print(f'Você acabou de digitar o número {n}')

