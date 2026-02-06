a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
menor = a
if b < menor:
    menor = b
if c <  menor:
    menor = c
print(f'O menor número é o: {menor}')
maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c
print(f'O maior número é o: {maior}')
