from time import sleep
def maior (*valores):
    maior_atual = valores[0]
    for num in valores:
        if num > maior_atual:
            maior_atual = num
    cont = len(valores)
    print(f'Analisando os valores informados...')
    sleep(1)
    print(f'os valores digitados foram: {valores}, portanto ao todo foi informado {cont} termos.')
    print(f'O maior valor informado foi {maior_atual}')

maior(1,12,8)