print('=' * 50)
print(f'{"BEM VINDO AO MAIOR BANCO DO BRASIL":^50}')
print('=' * 50)
valor = int(input('Qual valor você quer sacar? R$ '))
total = valor
cedula_atual = 50
total_cedulas = 0
while True:
    if total >= cedula_atual:
        total -= cedula_atual
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print(f'Total de {total_cedulas} cédulas de R$ {cedula_atual}')
        if cedula_atual == 50:
            cedula_atual = 20
        elif cedula_atual == 20:
            cedula_atual = 10
        elif cedula_atual == 10:
            cedula_atual = 1
        total_cedulas = 0
        if total == 0:
            break
print('=' * 50)
print('Saque finalizado com sucesso. Volte sempre!')