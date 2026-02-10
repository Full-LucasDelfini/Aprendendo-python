valor = float(input('Qual o valor da casa que deseja comprar? '))
salario = float(input('Qual o seu sálario atual? '))
anos = float(input('Em quantos anos deseja comprar? '))
parcela = valor / (anos * 12)
if parcela < salario * 0.3:
    print('\033[32;40mVocê poderá comprar a casa!',end=' ')
    print(f'\033[32;40m A prestação será de R$: {parcela:.2f}\033[m')
elif parcela == salario * 0.3:
    print('\033[33;40mVocê está no limite para comprar a casa, tome cuidado!',end=' ')
    print(f'\033[33;40m A parcela de R$: {parcela:.2f}\033[m')
else:
    print('\033[31;40m Você ainda não tem condições para comprar a casa,',end=' ')
    print(f'\033[31;40m pois a parcela de R$: {parcela:.2f} excede 30% do seu sálario de R${salario:.2f}\033[m')