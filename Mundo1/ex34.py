money = float(input('Digite o sálario atual em reais: R$ '))
if money <= 1250:
    print(f'Você recebeu um aumento de 15%, logo seu novo sálario será: R$ {money * 1.15:.2f}')
else:
    print(f'Você recebeu um aumento de 10%, logo seu novo sálario será: R$ {money * 1.10:.2f}')
