from ex109 import moeda
v = float(input('Digite um valor: '))
print(f'A metade de {moeda.moeda(v)} é: {moeda.metade(v, True)}')
print(f'O dobro de {moeda.moeda(v)} é: {moeda.dobro(v, True)}')
print(f'Aumentando 10% temos {moeda.aumentar(v, 10, True)}')
print(f'Diminuindo 15% temos {moeda.diminuir(v, 15, True)}')