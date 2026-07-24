from ex107 import moeda
v = float(input('Digite um valor: '))
print(f'A metade de {v} é: {moeda.metade(v)}')
print(f'O dobro de {v} é: {moeda.dobro(v)}')
print(f'Aumentando 10%, temos {moeda.aumentar(v,10)}')
print(f'Diminuindo 15% temos {moeda.diminuir(v, 15)}')