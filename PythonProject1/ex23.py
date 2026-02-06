num = int(input('Digite um número: '))
uni = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10
print(f'A unidade é {uni}\n A dezena é {dez}\n A centena é {cen}\n O milhar é {mil}')
