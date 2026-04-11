while True:
    num = int(input('Qual valor você quer mostrar a tabuada? '))
    if num <= 0:
        print('Programa encerrado, pois você digitou números menores que 0 ou inválidos')
        break
    for c in range(1, 11):
        print(f'{num} x {c:2} = {num * c:2}')
print('Programa finalizado com sucesso! Volte sempre!')
