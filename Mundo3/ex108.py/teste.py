from ex108 import moeda
v = float(input('Digite um valor: '))
print(f'A metade de {moeda.moeda(v)} é: {moeda.moeda(moeda.metade(v))}')
print(f'O dobro de {moeda.moeda(v)} é: {moeda.moeda(moeda.dobro(v))}')
print(f'Aumentando 10% temos {moeda.moeda(moeda.aumentar(v, 10))}')
print(f'Diminuindo 15% temos {moeda.moeda(moeda.diminuir(v, 15))}')
